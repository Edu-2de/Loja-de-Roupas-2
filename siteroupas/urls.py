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
    path('criar-categoria/', views.criar_categoria, name='criar_categoria'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('profile/', views.user_profile, name='user_profile'),
    


]
# Adiciona URLs para arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
