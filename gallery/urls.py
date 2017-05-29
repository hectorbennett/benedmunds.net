from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^artwork/$', views.artwork, name='artwork'),
	url(r'^artwork/(?P<pk>\d+)/$', views.artwork_detail, name='artwork_detail'),
	url(r'^artwork/fullscreen/(?P<pk>\d+)/$', views.artwork_fullscreen, name='artwork_fullscreen'),
]
