from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^qs/$', views.qs),
    url(r'^get_body_form$', views.get_body_form),
    url(r'^get_body_json$', views.get_body_json),
    url(r'^demo_view$', views.demo_view),
]