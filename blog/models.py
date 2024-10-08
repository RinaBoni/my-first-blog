from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):       #Означает, что объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Метод публикации записи, заполняется дата публикации"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Возвращает строку - название поста"""
        return self.title


