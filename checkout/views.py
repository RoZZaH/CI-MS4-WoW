from re import template
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.conf import settings
import stripe

from .forms import OrderForm
from django.views import View
from django.views.generic import DetailView, TemplateView
from basket.contexts import basket_contents
from .models import Order, OrderLineItem
from wines.models import Wine

class CheckoutView(View):
# Display Form
# on error - display validation errors
# on success redirect to success url

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
            order = order_form.save()
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



# def checkout_success(request, order_number):
#     save_info = request.session.get("save_info")
#     order = get_object_or_404(Order, order_number=order_number)
    
#     messages.success(request, f"Order successfully processed! \
#             Your order number is {order_number}. \
#             A confirmation email will be sent to {order.email}")

#     if "basket" in request.session:
#         del request.session["basket"]
    
#     template = "checkout_success.html"
#     context = {
#         "order": order,
#     }
#     return render(request, template, context)

class CheckoutSuccessView(TemplateView): #DetailView requires slug or pk
    model = Order
    template_name = "checkout_success.html"
    # save_info = request.session.get("save_info")
    
    def setup(self, request, *args, **kwargs):
        print("baseket removed")
        return super().setup(request, *args, **kwargs)

    
    # success_message = tt
 
    
    def get_context_data(self, **kwargs):
        # del signal on Orser.save()
        order_number = self.kwargs["order_number"]
        order = self.model.objects.get(order_number=order_number)
        messages.success(self.request, (f"Order successfully processed! \
            Your order number is {order_number}. \
            A confirmation email will be sent to {order.email}"))
        context = super().get_context_data(**kwargs)
        context["order"] = order
        return context
    

    # (self):
    #     qs = super().get_queryset()
    #     return qs.filter(order_number=self.order_number)

    

    
    # context = {
    #     "order": order,
    # }
    # return render(request, template, context)
