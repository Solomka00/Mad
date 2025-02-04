from django.urls import path
from . import views
from articles.views import home
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path("LBLB/index.html", home),  # Главная страница
    path('', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # Новый URL для подробностей
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)