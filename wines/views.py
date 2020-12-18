from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Wine

class WineListView(ListView):
    
    template_name = "wines_list.html"
    model = Wine
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            return qs.filter(Q(name__icontains=q) | Q(description__icontains=q))
        return qs


class WineTypeView(ListView):

    template_name = "wines_list.html"
    model = Wine
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
        return Wine.objects.filter(wtype__icontains=self.kwargs.get('wtype'))


class WineDetailView(DetailView):

    template_name = "wines_detail.html"
    model = Wine


class WineSpecials(ListView):
    
    template_name = "wines_list.html"
    model = Wine
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(discounted_price__isnull=False)
