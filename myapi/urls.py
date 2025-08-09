from django.urls import path, include
from . import views

urlpatterns = [
    path('items/', views.item_list ,name='item-list'),
]