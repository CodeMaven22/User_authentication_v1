from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def lecturers_dashboard(request):
    if request.user.role != 'lecturer':
        return HttpResponse("Access denied.")
    return render(request, 'Lecturers/lecturers_dashboard.html')