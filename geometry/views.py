from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'geometry/geometry_maintenance.html')


def geometry_7_1_1(request):
    return render(request, "geometry/7 class/geometry_7_1_1.html")


