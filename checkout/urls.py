from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [
     path(
        route='',
        # view = views.checkout,
        view = views.CheckoutView.as_view(),
        name='list'
    ),
     path(
        route='success/<order_number>/',
        # view = views.checkout,
        view = views.CheckoutSuccessView.as_view(),
        name='success'
    ),
    # path(
    #     route='checkout_success/<order_number>/',
    #     view = views.checkout_success,
    #     name='success'
    # ),
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
