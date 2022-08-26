
from django.contrib import admin
from django.urls import path,include
from django import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls')),
    #path('col/', include('colc.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)