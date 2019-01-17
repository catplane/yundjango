from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializers import BookInfoSerializer
from .models import BookInfo
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class BookInfoViewSet(ViewSet):
    def list(self,request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            books = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoSerializer(books)
        return Response(serializer.data)


# class BookInfoViewSet(ModelViewSet):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer


from rest_framework.views import APIView
from rest_framework.response import Response


# class BookListView(APIView):
#     def get(self, request):
#         books = BookInfo.objects.all()
#         serializer = BookInfoSerializer(books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         json_str = request.data
#         book = BookInfoSerializer(data=json_str)
#         # book.is_valid(raise_exception=True)
#         book.save()
#         return Response('xixi')

# class BookListView(ListModelMixin, GenericAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#
#     def get(self, request):
#         return self.list(request)


# class BookDetailView(GenericAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#
#     def get(self, request, pk):
#         book = self.get_object() # get_object()方法根据pk参数查找queryset中的数据对象
#         serializer = self.get_serializer(book)
#         # print(serializer)
#         return Response(serializer.data)


# class BookDetailView(RetrieveModelMixin, GenericAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request)

# class BookListView(ListAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer





