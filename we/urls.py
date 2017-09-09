import os
from django.conf.urls import url
from . import views
from django.views.static import serve


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(BASE_DIR, 'we/static/images').replace('\\', '/')
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mvBrick$', views.mvBrick),
    url(r'^static/images/(?P<path>.*)$', serve, {'document_root': IMAGE_DIR}),
]
