from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def maintenance(request):
    return render(request, "main/maintenance.html")


def about(request):
    return render(request, "main/about.html")


