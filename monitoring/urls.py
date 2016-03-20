from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^putDatas', views.putDatas, name='putDatas'),
]
