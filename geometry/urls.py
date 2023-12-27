from django.urls import path
from . import views
# При переходе по адресу admin/ будет открываться приложение admin
# (панель администратора, установлена по умолчанию в любом Джанго проекте)
urlpatterns = [
    path('7_class/1_chapter/1_lesson', views.geometry_7_1_1, name='geometry_7_1_1'),
    path('7_class/2_chapter/1_lesson', views.geometry_7_2_1, name='geometry_7_2_1'),
    path('7_class/2_chapter/2_lesson', views.geometry_7_2_2, name='geometry_7_2_2'),
    path('7_class/2_chapter/3_lesson', views.geometry_7_2_3, name='geometry_7_2_3'),
    path('7_class/2_chapter/4_lesson', views.geometry_7_2_4, name='geometry_7_2_4'),
    path('7_class/2_chapter/5_lesson', views.geometry_7_2_5, name='geometry_7_2_5'),
    path('7_class/2_chapter/6_lesson', views.geometry_7_2_6, name='geometry_7_2_6'),
]