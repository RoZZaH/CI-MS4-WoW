from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models.functions import Coalesce

from .models import Wine

class WineListView(ListView):
    
    template_name = "wines_list.html"
    model = Wine
    paginate_by = 12

   
    def get_queryset(self):
        # qs = super().get_queryset()
        qs = self.model.objects.all()

        def getDirection():
            return '-' if 'direction' in self.request.GET and self.request.GET['direction'] == 'desc' else ''

        sortkey = self.request.GET.get("sort")
        sort = sortkey
        if sortkey == 'list_price':
            dir = getDirection()
            qs = Wine.objects.annotate(final_price=Coalesce('discounted_price','list_price')).order_by(f'{dir}final_price')
            # sortkey = 'lower_name'
            # if "direction" in self.request.GET.get("direction") and self.request.GET.get("direction"):
            #     sortkey = f'-{sortkey}'

        if sortkey == 'wtype':
            dir = getDirection()
            qs = Wine.objects.order_by(f'{dir}wtype')

        if sortkey == 'star_rating':
            dir = getDirection()
            qs = Wine.objects.order_by(f'{dir}star_rating')

        q = self.request.GET.get("q")
        if q:
            qs = self.model.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
        return qs
    

    # def get_from_kwargs(self):
    #     kwargs = super(WineListView, self).get_from_kwargs()
    #     if 'sort' in self.request.GET:
    #         current_sorting = f'{ self.request.GET["sort"] }_{self.request.GET["direction"]}'
    #         kwargs['current_sorting'] = current_sorting
    #     return kwargs
    def get_context_data(self, **kwargs):
        ctx = super(WineListView, self).get_context_data(**kwargs)
        if 'sort' in self.request.GET:
            current_sorting = f'{ self.request.GET["sort"] }|{self.request.GET["direction"]}'
            ctx['current_sorting'] = current_sorting
        if 'q' in self.request.GET:
            ctx['search_term'] = self.request.GET["q"]
        return ctx

    



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
