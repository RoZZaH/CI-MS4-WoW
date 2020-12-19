from django.urls import path
from . import views

app_name = "basket"
urlpatterns = [
    path(
        route='',
        view = views.BasketListView.as_view(),
        name='list'
    ),
    path(
        route='add/<slug>/',
        view = views.add,
        name='add'
    ),
]