from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
 

    basket = request.session.get("basket")
    if not basket:
        messages.error(request, "Your basket is currently empty!")
        return redirect(reverse("wines:list"))
    
    order_form = OrderForm()
    template = "checkout_list.html"
    context = {
        "order_form": order_form,
        "stripe_public_key" : stripe_public_key,
        "client_secret": stripe_secret_key

    }

    return render(request, template, context)