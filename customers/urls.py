from django.urls import path
from . import views

app_name = "customers"

urlpatterns = [
  path(
        route='',
        view = views.CustomerProfile.as_view(),
        name='profile'
    ),
  path(
        route = 'order_history/<order_number>/',
        view = views.OrderHistory.as_view(),
        name='order_history'
    ),

]