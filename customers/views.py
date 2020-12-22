# from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, TemplateView


class CustomerProfile(TemplateView):
    template_name = "customers_profile.html"
