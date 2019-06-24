# Create your models here.
# Строки, начинающиеся с from или import, открывают доступ к коду из других файлов.
from django.conf import settings
from django.db import models
from django.utils import timezone

# Cтрока определяет нашу модель (объект).
# Class — это специальное ключевое слово для определения объектов.
# Post — это имя нашей модели, мы можем поменять его при желании (специальные знаки и пробелы использовать нельзя). Всегда начинай имена классов с прописной буквы.
# models.Model означает, что объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных.
# models.ForeignKey — ссылка на другую модель.

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
# Метод публикации для записи.
	def publish(self):
		self.published_date = timezone.now()
		self.save()
# Методы часто возвращают что-то. Например, метод __str__. В наше случае после вызова метода __str__() мы получим текст (строку) с заголовком записи.
	def __str__(self):
		return self.title