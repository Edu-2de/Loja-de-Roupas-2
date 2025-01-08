from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from siteroupas_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),  
    path('create_product/', views.create_product, name='create_product'),
    path('create-brand/', views.create_brand, name='create_brand'),
    path('create-banner/', views.create_banner, name='create_banner'),
    path('create-category/', views.create_category,name='create_category'),
    path('create-color/', views.create_color,name='create_color'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('profile/', views.user_profile, name='user_profile'),
    


]
# Adiciona URLs para arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
