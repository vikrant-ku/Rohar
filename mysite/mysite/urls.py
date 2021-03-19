from django.contrib import admin
from django.urls import path, include
from rohartech import views
from django.conf.urls.static import static
from . import settings

admin.site.site_header = 'RoharTech admin'
admin.site.site_title = 'RoharTech admin'
admin.site.site_url = ' http://127.0.0.1:8000/'
admin.site.index_title = 'RoharTech administration'
admin.empty_value_display = '**Empty**'

handler404 = views.error_404
handler500 = views.error_500

urlpatterns = [
    path('rohar/tech/admin/', admin.site.urls),
    path('', include('rohartech.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)