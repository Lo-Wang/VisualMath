from django.urls import path
from . import views
# При переходе по адресу admin/ будет открываться приложение admin
# (панель администратора, установлена по умолчанию в любом Джанго проекте)
urlpatterns = [
    path('', views.index, name='geometry_maintenance'),
    path('7_class/1_chapter/1_lesson', views.geometry_7_1_1, name='geometry_7_1_1'),
]