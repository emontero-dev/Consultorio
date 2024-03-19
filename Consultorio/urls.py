
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Login.urls')),
    path('Pacientes/', include('Pacientes.urls'), name='Pacientes'),
    path('Dentistas/', include('Dentistas.urls'), name='Dentistas'),
    path('Facturacion/', include('MetodosPago.urls'), name='Facturacion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
