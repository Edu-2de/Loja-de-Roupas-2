from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from siteroupas_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),  
    path('criar_produto/', views.criar_produto, name='criar_produto'),
    path('criar-marca/', views.criar_marca, name='criar_marca'),
    path('criar-banner/', views.criar_banner, name='criar_banner'),


]
# Adiciona URLs para arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
