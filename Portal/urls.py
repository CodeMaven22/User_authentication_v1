from django.urls import path
from . import views

urlpatterns = [
    path('Portal/', views.student_portal, name='students_portal')
]
