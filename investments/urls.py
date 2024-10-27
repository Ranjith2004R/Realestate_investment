from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('property/<int:property_id>/invest/', views.invest, name='invest'),
    path('property/add/', views.add_property, name='add_property'),
]
