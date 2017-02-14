from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^log_out$',views.log_out),
    url(r'^add$',views.add),
    url(r'^item_create$', views.item_create),
    url(r'^item_remove/(?P<id>\d+)$',views.item_remove),
    url(r'^item_delete/(?P<id>\d+)$',views.item_delete),
    url(r'^item_show/(?P<id>\d+)$',views.item_show),
    url(r'^item_added/(?P<id>\d+)$',views.item_added), 
]
