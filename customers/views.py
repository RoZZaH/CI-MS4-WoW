from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, TemplateView, FormView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Customer
from .forms import CustomerForm

from checkout.models import Order


class CustomerProfile(UpdateView):
    template_name = "customers_profile.html"
    model = Customer
    form_class = CustomerForm

    def get_object(self, **kwargs):
        obj = self.model.objects.get(user=self.request.user)
        return obj

    def get_context_data(self, **kwargs):
        orders = self.get_object().orders.all().order_by('-date')
        context = super().get_context_data(**kwargs)
        context["orders"] = orders
        context["on_profile_page"] = True
        return context
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Profile updated successfully")
        return reverse("customers:profile")


class OrderHistory(DetailView):

    model = Order
    template_name = "checkout_success.html"

    def get_object(self, **kwargs):
        order_number = self.kwargs["order_number"]
        order = self.model.objects.get(order_number=order_number)
        return order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["from_profile"] = True
        return context

