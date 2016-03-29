from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hives/$', views.seeHives, name='seeHives'),
    url(r'^hive/(?P<idHive>[0-9]+)$', views.seeHive, name='seeHive'),
    url(r'^hive/(?P<idHive>[0-9]+)/(?P<idCaptor>[0-9]+)$', views.seeCaptor, name='seeCaptor'),
    url(r'^putDatas', views.putDatas, name='putDatas'),
]
