from django.conf.urls import url
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from booktest import views

urlpatterns = [
    # url(r'^books/$', views.BooksAPIVIew.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view())
    # url(r'^books/$', views.BookListView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
    # url(r'^books/$', views.BookInfoViewSet.as_view({'get': 'list'})),
    # url(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({'get': 'retrieve'})),
    # url(r'^books/$', views.BookInfoViewSet.as_view({'get': 'list'})),
    # url(r'^books/latest/$', views.BookInfoViewSet.as_view({'get': 'latest'})),
    # url(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({'get': 'retrieve'})),
    # url(r'^books/(?P<pk>\d+)/read/$', views.BookInfoViewSet.as_view({'put': 'read'})),

]

# router = DefaultRouter()
# router.register(r'books', views.BookInfoViewSet)
# urlpatterns += router.urls

# DefaultRouter与SimpleRouter的区别是，
# DefaultRouter会多附带一个默认的API根视图，返回一个包含所有列表视图的超链接响应数据。
router = routers.SimpleRouter()
router.register(r'books', views.BookInfoViewSet, base_name='book')
urlpatterns += router.urls