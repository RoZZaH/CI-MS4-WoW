from django.urls import path
from . import views

app_name = "wines"
urlpatterns = [
    path(
        route='',
        view = views.WineListView.as_view(),
        name='list'
    ),
    path(
        route='specials/',
        view=views.WineSpecials.as_view(),
        name='specials'),
    path(
        route='type/<str:wtype>/',
        view=views.WineTypeView.as_view(),
        name='type'),
    path(
        route='<slug:slug>/',
        view=views.WineDetailView.as_view(),
        name='detail'
    ),
]