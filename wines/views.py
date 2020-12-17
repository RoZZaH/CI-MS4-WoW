from django.views.generic import ListView, DetailView

from .models import Wine

class WineListView(ListView):
    template_name = "wines_list.html"
    model = Wine


class WineDetailView(DetailView):
    template_name = "wines_detail.html"
    model = Wine