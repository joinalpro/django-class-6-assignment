from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.seo),
    path('seo-check/', views.seo_checklist),
    
]