from django.urls import path, re_path
from . import views


app_name = 'customers'
urlpatterns = [
    path('add', views.add_customer, name='add_customer'),
    path('<int:customer_id>/edit', views.edit_customer, name="edit_customer"),
    path('', views.list_customers, name='list_customers'),
    path('notfound', views.notfound, name="notfound"),
]
