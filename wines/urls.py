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
        route='add/',
        view=views.AddWine.as_view(),
        name='add'),
    path(
        route='edit/<slug:slug>/',
        view=views.EditWine.as_view(),
        name='edit'),
    path(
        route='delete/<slug:slug>/',
        view=views.DeleteWine.as_view(),
        name='delete'),
    path(
        route='type/<str:wtype>/',
        view=views.WineListView.as_view(),
        name='type'),
    path(
        route='<slug:slug>/',
        view=views.WineDetailView.as_view(),
        name='detail'
    ),
]