from django.urls import path
from .views import (
    index, client_list, client_create, client_update, client_delete,
    employee_list, employee_create, employee_update, employee_delete,
    item_list, item_create, item_update, item_delete,
    worktype_list, worktype_create, worktype_update, worktype_delete,
    servicecost_list, servicecost_create, servicecost_update, servicecost_delete
)

urlpatterns = [
    path('', index, name='index'),
    path('clients/', client_list, name='client_list'),
    path('clients/new/', client_create, name='client_create'),
    path('clients/<int:pk>/edit/', client_update, name='client_update'),
    path('clients/<int:pk>/delete/', client_delete, name='client_delete'),

    path('employees/', employee_list, name='employee_list'),
    path('employees/new/', employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', employee_delete, name='employee_delete'),

    path('items/', item_list, name='item_list'),
    path('items/new/', item_create, name='item_create'),
    path('items/<int:pk>/edit/', item_update, name='item_update'),
    path('items/<int:pk>/delete/', item_delete, name='item_delete'),

    path('worktypes/', worktype_list, name='worktype_list'),
    path('worktypes/new/', worktype_create, name='worktype_create'),
    path('worktypes/<int:pk>/edit/', worktype_update, name='worktype_update'),
    path('worktypes/<int:pk>/delete/', worktype_delete, name='worktype_delete'),

    path('servicecosts/', servicecost_list, name='servicecost_list'),
    path('servicecosts/new/', servicecost_create, name='servicecost_create'),
    path('servicecosts/<int:pk>/edit/', servicecost_update, name='servicecost_update'),
    path('servicecosts/<int:pk>/delete/', servicecost_delete, name='servicecost_delete'),
]
