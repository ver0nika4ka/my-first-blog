# Так мы импортировали функцию path Django и все views (представления) из приложения blog
from django.urls import path
from . import views


urlpatterns = [
	path('', views.post_list, name='post_list'),
	# Фрагмент post/<int:pk>/ определяет шаблон URL-адреса:
	# post/ значит, что после начала строки URL должен содержать слово post и косую черту /.
	# <int:pk> — эта часть означает, что Django ожидает целочисленное значение и преобразует его в представление — переменную pk.
	# / — затем нам нужен еще один символ / перед тем, как адрес закончится.
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]