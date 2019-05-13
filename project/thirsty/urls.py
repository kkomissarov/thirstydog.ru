from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from public.sitemaps import sitemaps



urlpatterns = [
    path('', include('public.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'public.views.page404'