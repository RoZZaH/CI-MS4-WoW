import django
from django.shortcuts import redirect, render, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get("basket")
    if not basket:
        messages.error(request, "Your basket is currently empty!")
        return redirect(reverse("wines:list"))
    
    order_form = OrderForm()
    template = "checkout_list.html"
    context = {
        "order_form": order_form
    }

    return render(request, template, context)