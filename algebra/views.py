from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'algebra/algebra_maintenance.html')


def first_tema(request):
    return render(request, "algebra/7 class/first_tema.html")


