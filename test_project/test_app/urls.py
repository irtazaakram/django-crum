# Django
try:
    from django.urls import path
except ImportError:
    from django.conf.urls import url as path

# Test App
from test_project.test_app.views import api_index, index

app_name = 'test_app'

urlpatterns = [
    path('', index, name='index'),
    path('api/', api_index, name='api_index'),
]
