from django.conf.urls import url

from classview import views

urlpatterns = [
    # 在URL配置中装饰,此种方式会为类视图中的所有请求方法都加上装饰器行为
    # url(r'demo/$', views.my_decorator(views.DemoView.as_view()))
    url(r'^demo/$', views.DemoView.as_view()),
    url(r'^demo_Mixin$', views.BooksView.as_view()),
]