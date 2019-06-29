# Так мы импортировали функцию path Django и все views (представления) из приложения blog
from django.urls import path
from . import views


urlpatterns = [
	path('', views.post_list, name='post_list'),
]