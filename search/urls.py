from django.conf.urls import url
from .views import to_search

urlpatterns = [
    url(r'^$', to_search, name="search")
    ]