from django.conf.urls import url

from register import views

urlpatterns = [
    #视图函数：注册
    # url(r'^register/$', views.register, name='register')
    #类视图：注册
    url(r'register/$', views.RegisterView.as_view(), name='register')

]