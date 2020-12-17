import django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('wines/', include('wines.urls', namespace='wines')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
