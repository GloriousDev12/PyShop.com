from django.urls import path

from . import views


urlpatterns = [

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'confirmation/',
        views.order_confirmation,
        name='order_confirmation'
    ),

    path(
        'history/',
        views.order_history,
        name='order_history'
    ),

    path(
        'history/<int:order_id>/',
        views.order_detail,
        name='order_detail'
    ),

]