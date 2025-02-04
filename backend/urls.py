from django.shortcuts import render  # Импортируем render
from django.contrib import admin
from django.urls import path, include
from articles.views import home
from articles import views
from django.conf.urls.static import static
from django.conf import settings
def home(request):
    return render(request, 'articles/')

urlpatterns = [

    path("articles/index.html/", home),  # Главная страница
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),  # Подключаем URL-ы приложения
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
