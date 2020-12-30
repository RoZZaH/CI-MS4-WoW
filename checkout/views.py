from re import template
from django.shortcuts import get_object_or_404, redirect, render, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import stripe
import json

from .forms import OrderForm
from django.views import View
from django.views.generic import DetailView, TemplateView
from basket.contexts import basket_contents
from .models import Order, OrderLineItem
from wines.models import Wine
from customers.models import Customer
from customers.forms import CustomerForm


@require_POST
def cache_checkout_payform_data(request):
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket')),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Sorry, your payment cannot be \
            processed right now. Please try again later.")
        return HttpResponse(content=e, status=400)



class CheckoutView(View):  

    form_class = OrderForm

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    template = "checkout_payform.html"

    def get(self,request,*args,**kwargs):
        # basket = request.session.get("basket")
        if not request.session.get("basket"):
            messages.error(request, "Your basket is currently empty!")
            return redirect(reverse("wines:list"))

        basket = basket_contents(request)
        stripe_total = round(basket["grand_total"] * 100)
        stripe.api_key = self.stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = Customer.objects.get(user=request.user)
                order_form = self.form_class(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.primary_phone_number,
                    'country': profile.primary_country,
                    'postcode': profile.primary_postcode,
                    'town_or_city': profile.primary_town_or_city,
                    'street_address1': profile.primary_street_address1,
                    'street_address2': profile.primary_street_address2,
                    'county': profile.primary_county,
                })
            except Customer.DoesNotExist:
                order_form = self.form_class()
        else:
            order_form = self.form_class()

        if not self.stripe_public_key:
            messages.warning(request, ('Stripe public key is missing. '
                                        'Did you forget to set it?! (hint:env)'))

        context = {
            "order_form": order_form,
            "stripe_public_key" : self.stripe_public_key,
            "client_secret": intent.client_secret
        }

        return render(request, self.template, context)

    def post(self,request,*args,**kwargs):
    
        basket = request.session.get("basket", {})

        form_data = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'country': request.POST.get('country'),
            'postcode': request.POST.get('postcode'),
            'town_or_city': request.POST.get('town_or_city'),
            'street_address1': request.POST.get('street_address1'),
            'street_address2': request.POST.get('street_address2'),
            'county': request.POST.get('county'),
        }

        order_form = self.form_class(form_data or None)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()

            for bottle_id, quantity in basket.items():
                try:
                    product = Wine.objects.get(slug=bottle_id)
                    _price =  (product.discounted_price if product.discounted_price \
                                is not None else product.list_price)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save(price=_price) #post save signal
                    
                except Wine.DoesNotExist:
                        messages.error(request, (
                            "One of the products in your basket wasn't "
                            "found in our database. "
                            "Please call us for assistance!")
                        )
                        order.delete()
                        return redirect(reverse('basket:list'))

            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("checkout:success", args=[order.order_number]))
        else:
            messages.error(request, "There is nothing in your basket at the moment \
                Please double-check your information")
            return redirect(reverse("checkout:list"))



class CheckoutSuccessView(TemplateView): #DetailView requires slug or pk
    model = Order
    template_name = "checkout_success.html"

    def get_object(self, **kwargs):
        save_info = self.request.session.get("save_info")
        order_number = self.kwargs["order_number"]
        order = self.model.objects.get(order_number=order_number)
        if self.request.user.is_authenticated:
            profile = Customer.objects.get(user=self.request.user)
            # Attach the user's profile to the order
            order.customer = profile
            order.save()

            # Save the user's info
            if save_info:
                profile_data = {
                    'primary_phone_number': order.phone_number,
                    'primary_country': order.country,
                    'primary_postcode': order.postcode,
                    'primary_town_or_city': order.town_or_city,
                    'primary_street_address1': order.street_address1,
                    'primary_street_address2': order.street_address2,
                    'primary_county': order.county,
                }
                customer_profile_form = CustomerForm(profile_data, instance=profile)
                if customer_profile_form.is_valid():
                    customer_profile_form.save()
        return order


    def get_context_data(self, **kwargs):
        order = self.get_object()
        if 'basket' in self.request.session:
            del self.request.session['basket']
        messages.success(self.request, (f"Order successfully processed! \
            Your order number is {order.order_number}. \
            A confirmation email will be sent to {order.email}"))
        context = super().get_context_data(**kwargs)
        context["order"] = order
        context["from_profile"] = True
        return context
    
