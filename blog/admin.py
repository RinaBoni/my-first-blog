from django.contrib import admin
from .models import Post

#Чтобы модель Post стала доступна на странице администрирования, нужно зарегистрировать
admin.site.register(Post)


