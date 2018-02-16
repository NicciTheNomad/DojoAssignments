from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs$', views.index),
    url(r'^blogs/new$', views.new),
    url(r'^blogs/create$', views.create),
    url(r'^blogs/display$', views.display),
    url(r'^blogs/(?P<blog_id>\d+)', views.show),
    url(r'^blogs/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^blogs/(?P<blog_id>\d+)/delete$', views.delete)
]
