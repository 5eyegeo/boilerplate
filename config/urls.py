from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.views import index

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", index, name="home"),
    # path('accounts/', include('allauth.urls')),
    # path("", include('projects.helloworld.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'config.views.handler404'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
