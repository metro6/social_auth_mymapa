from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns


from . import views as social_auth_mymapa


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include('apps.api.urls')),
    url(r'user/', include('apps.user.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
]

urlpatterns += i18n_patterns(
    url(r'^$', social_auth_mymapa.main, name="home"),
    prefix_default_language=True,
)


if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
