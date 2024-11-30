from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from siteroupas_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),  
]
