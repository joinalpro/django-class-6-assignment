from django.urls import path
from . import views

urlpatterns = [
    path('link-building/', views.linkbuilding),
    path('lb-list/', views.link_building_list),
    
]