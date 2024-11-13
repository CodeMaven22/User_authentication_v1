from django.urls import path
from . import views

urlpatterns = [
    path('Dashboard/', views.lecturers_dashboard, name='lecturers_dashboard')
]
