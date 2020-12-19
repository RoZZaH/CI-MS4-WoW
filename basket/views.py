from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import redirect

class BasketListView(TemplateView):

    template_name = "basket_list.html"


def add(request, slug):
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    basket = request.session.get("basket", {})

    if slug in list(basket.keys()):
        basket[slug] += quantity
    else:
        basket[slug] = quantity

    request.session["basket"] = basket
    # print(request.session["basket"])
    return redirect(redirect_url)
