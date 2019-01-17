from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from booktest import views

urlpatterns = [
    # url(r'^books/$', views.BooksAPIVIew.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view())
    # url(r'^books/$', views.BookListView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
    url(r'^books/$', views.BookInfoViewSet.as_view({'get': 'list'})),
    url(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({'get': 'retrieve'})),
]

# router = DefaultRouter()
# router.register(r'books', views.BookInfoViewSet)
# urlpatterns += router.urls
