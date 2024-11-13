from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def registrar_dashboard(request):
    if request.user.role != 'registrar':
        return HttpResponse("Access denied.")
    # Business logic for staff
    return render(request, 'Registrars/registrar_dashboard.html')