from django.shortcuts import render  # Импортируем render
from django.contrib import admin
from django.urls import path, include

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path("LBLB/index.html", home),  # Главная страница
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),  # Подключаем URL-ы приложения
]
