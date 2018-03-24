from django.conf.urls import url
from .views import createMsg , allMessage

urlpatterns = [
    url(r'^$' , createMsg , name='createmessage'),
    url(r'^allmessage/' , allMessage , name='allmessage'),
]