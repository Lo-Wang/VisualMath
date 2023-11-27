from django.urls import path
from . import views
# При переходе по адресу admin/ будет открываться приложение admin
# (панель администратора, установлена по умолчанию в любом Джанго проекте)
urlpatterns = [
    path('', views.index, name='home'),
    path('content', views.content, name='content'),
    path('maintenance', views.maintenance, name='maintenance'),
]
