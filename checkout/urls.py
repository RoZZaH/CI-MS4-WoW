from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [
     path(
        route='',
        view = views.checkout,
        name='list'
    )
    # path(
    #     route='add/<slug>/',
    #     view = views.add,
    #     name='add'
    # ),
    # path(
    #     route='adjust/<slug>/',
    #     view = views.adjust,
    #     name='adjust'
    # ),
    # path(
    #     route='remove/<slug>/',
    #     view = views.remove,
    #     name='remove'
    # ),
]
