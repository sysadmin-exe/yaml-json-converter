from django.conf.urls import url, include
from yasonapi import views
from yasonapi.views import *

urlpatterns = [ 
    url(r'^api/yason/yaml-to-json$', views.yaml_to_json),
    url(r'^api/yason/json-to-yaml$', views.json_to_yaml),
    url(r'^api/yason/health$', views.getHealth) 

]
