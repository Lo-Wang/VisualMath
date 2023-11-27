from django.urls import path
from . import views
# При переходе по адресу admin/ будет открываться приложение admin
# (панель администратора, установлена по умолчанию в любом Джанго проекте)
urlpatterns = [
    path('', views.index, name='algebra_maintenance'),
    path('first_tema', views.first_tema, name='first_tema'),
]