from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'geometry/geometry_maintenance.html')


def first_tema(request):
    return render(request, "geometry/7 class/first_tema.html")


