from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('troca_gelo.urls')),
]

# Servir arquivos de media em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Customização do Admin
admin.site.site_header = "Administração - Troca de Gelo 5S"
admin.site.site_title = "Troca de Gelo 5S"
admin.site.index_title = "Painel de Controle"