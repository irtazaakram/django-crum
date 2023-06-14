# Django
from django.conf import settings

try:
    from django.urls import include, path
except ImportError:
    from django.conf.urls import url as path

include_kwargs = dict(namespace='test_app')

urlpatterns = [
    path('test_app/', include('test_project.test_app.urls', **include_kwargs)),
]

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns += [
        path('', admin.site.urls),
    ]

if 'django.contrib.staticfiles' in settings.INSTALLED_APPS and settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
