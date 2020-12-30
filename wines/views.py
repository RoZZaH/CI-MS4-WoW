from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.db.models.functions import Coalesce

from .models import Wine
from .forms import WineForm

class WineListView(ListView):
    
    template_name = "wines_list.html"
    model = Wine
    paginate_by = 12

   
    def get_queryset(self):
        # qs = super().get_queryset()
        # order_by if no sort key
        qs = self.model.objects.all()

        def getDirection():
            return '-' if 'direction' in self.request.GET and self.request.GET['direction'] == 'desc' else ''

        sortkey = self.request.GET.get("sort")
        sort = sortkey
        if sortkey == 'list_price':
            dir = getDirection()
            qs = Wine.objects.annotate(final_price=Coalesce('discounted_price','list_price')).order_by(f'{dir}final_price')
     
        if sortkey == 'wtype':
            dir = getDirection()
            qs = Wine.objects.order_by(f'{dir}wtype')

        if sortkey == 'vintage':
            dir = getDirection()
            qs = Wine.objects.order_by(f'{dir}vintage')

        if sortkey == 'star_rating':
            dir = getDirection()
            qs = Wine.objects.order_by(f'{dir}star_rating')

        q = self.request.GET.get("q")
        if q:
            qs = self.model.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
        return qs
  
  
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
    paginate_by = 12
    
    def get_queryset(self, *args, **kwargs):
        return Wine.objects.filter(wtype__icontains=self.kwargs.get('wtype'))


class WineDetailView(DetailView):

    template_name = "wines_detail.html"
    model = Wine


class WineSpecials(ListView):
    
    template_name = "wines_list.html"
    model = Wine
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(discounted_price__isnull=False)


class AccessControlMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect_to_login(
                self.request.get.full_path(),
                self.get_login_url(),
                self.get_redirect_field_name())
        if not self.has_permission():
            return redirect("/wines/")
        return super(AccessControlMixin, self).dispatch(request, *args, **kwargs)


class AddWine(AccessControlMixin, CreateView):
    # raise_exception = False
    permission_required = "wines.change_wines"
    # permission_denied_message = ""
    login_url = "/wines/"
    redirect_field_name = "next"

    form_class = WineForm
    template_name = "wines_add.html"

    def get_success_url(self):
        return reverse("wines:add")


class EditWine(AccessControlMixin, UpdateView):
    # raise_exception = True
    permission_required = "wines.change_wines"
    # permission_denied_message = ""
    login_url = "/wines/"
    # redirect_field_name = "next"

    model = Wine
    form_class = WineForm
    template_name = "wines_update.html"

    def get_object(self, queryset=None):
        instance = self.model.objects.get(slug=self.kwargs.get('slug',''))
        return instance

    def get_success_url(self, **kwargs):
        return reverse_lazy("wines:detail", kwargs={"slug": self.kwargs.get('slug','') })


class DeleteWine(AccessControlMixin, DeleteView):
    permission_required = "wines.change_wines"
    
    model = Wine
    template_name = "wines_confirm_delete.html"

    def get_object(self, queryset=None):
        instance = self.model.objects.get(slug=self.kwargs.get('slug',''))
        return instance

    def get_success_url(self, **kwargs):
        return reverse_lazy("wines:list")
    