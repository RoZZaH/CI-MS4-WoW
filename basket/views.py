from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, redirect, reverse
from django.contrib import messages

from wines.models import Wine

class BasketListView(TemplateView):

    template_name = "basket_list.html"


def add(request, slug):
    wine = get_object_or_404(Wine, slug=slug)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    basket = request.session.get("basket", {})

    if slug in list(basket.keys()):
        basket[slug] += quantity
        messages.success(request, f"Updated {wine.name} quantity to {basket[slug]} bottles.")
    else:
        basket[slug] = quantity
        messages.success(request, f"Added {wine.name} to your basket")

    request.session["basket"] = basket
    return redirect(redirect_url)


def adjust(request, slug):
    wine = get_object_or_404(Wine, slug=slug)
    quantity = int(request.POST.get("quantity"))

    basket = request.session.get("basket", {})

    if slug in list(basket.keys()):
        basket[slug] = quantity
        messages.success(request, f"Updated {wine.name} quantity to {basket[slug]} bottles.")
    else:
        basket.pop(slug)
        messages.success(request, f"Removed {wine.name} from basket.")

    request.session["basket"] = basket
    return redirect(reverse("basket:list"))


def remove(request, slug):
    wine = get_object_or_404(Wine, slug=slug)
    try:
        basket = request.session.get("basket", {})
        basket.pop(slug)
        messages.success(request, f"Removed {wine.name} from basket.")
        request.session["basket"] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)