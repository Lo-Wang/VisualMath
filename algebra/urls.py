from django.urls import path
from . import views
# При переходе по адресу admin/ будет открываться приложение admin
# (панель администратора, установлена по умолчанию в любом Джанго проекте)
urlpatterns = [
    path('7_class/1_chapter/1_lesson', views.algebra_7_2_1__4, name='algebra_7_2_1-4'),
]