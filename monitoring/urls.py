from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hive/(?P<idHive>\w+)$', views.seeHive, name='seeHive'),
    url(r'^putDatas', views.putDatas, name='putDatas'),
]
