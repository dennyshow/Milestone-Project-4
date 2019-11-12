from django.conf.urls import url
from .views import view_basket, add_to_basket, update_basket

urlpatterns =  [
    url(r'^$', view_basket, name="view_basket"),
    url(r'^add/(?P<id>\d+)', add_to_basket, name="add_to_basket"),
    url(r'^update/(?P<id>\d+)', update_basket, name="update_basket"),
    
    ]