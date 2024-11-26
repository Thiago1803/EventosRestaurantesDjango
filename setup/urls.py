from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    path('auth/', include('consumers.urls')),
    path('logout/', views.logout_view, name='logout'),
    
    path('vagas/', include('reservations.urls'))
]


#isso é para indicar rota para renderizar midias, como imagens
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)