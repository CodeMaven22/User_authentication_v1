from django.urls import path
from . import views

urlpatterns = [
    path('Dashboard/', views.registrar_dashboard, name='registrar_dashboard')
]
