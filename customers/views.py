from django.views import View
from django.views.generic import DetailView, TemplateView
from .models import Customer

class CustomerProfile(TemplateView):
    template_name = "customers_profile.html"
    model = Customer

    def get_context_data(self, **kwargs):
        profile = self.model.objects.get(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context["profile"] = profile
        return context