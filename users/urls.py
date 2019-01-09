from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^users/index/$', views.index, name='index'),
    url(r'^say/$', views.say, name='say'),
]