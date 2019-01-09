from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^users/index/$', views.index, name='index'),
    url(r'^say/$', views.say, name='say'),
    url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
    #命名参数按名字传递url(r'^weather/(？P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
]