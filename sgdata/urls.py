
from django.conf.urls import patterns, url
from sgdata import views

urlpatterns = patterns('',url(r'^$',views.index, name='index' ),  
                          url(r'^(?P<project>[\w]+)/(?P<exp>[\w]+)/(?P<field>[\w]+)$', views.get_field, name = 'get_field'),
                      )
