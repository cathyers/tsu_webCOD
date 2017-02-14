from django.conf.urls import url

from . import searchSQL

app_name = 'searchSQL'
urlpatterns = [
    url(r'^$', searchSQL.search_post, name='searchSQL'),
 #   url(r'^search_cod/$', searchSQL.search_post, name='searchSQL'),
]