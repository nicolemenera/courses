from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^actual_delete/(?P<id>\d+)$', views.actual_delete),
    
]
