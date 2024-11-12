from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    path('auth/', include('consumers.urls')),
    path('logout/', views.logout_view, name='logout'),
    
    path('vagas/', include('reservations.urls'))
]
