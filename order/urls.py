from django.urls import path

from order.views import add_user_order,  order_list

urlpatterns = [
    path('add-user-order', add_user_order),
        path('order_list/', order_list)
]
