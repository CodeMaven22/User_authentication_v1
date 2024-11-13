from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def student_portal(request):
    if request.user.role != 'student':
        return HttpResponse("Access denied.")
    # Business logic for student
    return render(request, 'Portal/portal.html')
