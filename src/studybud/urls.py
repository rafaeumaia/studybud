from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from apps.blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
]

apps_urlpatterns = [
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views')
]

urlpatterns.extend(apps_urlpatterns)
