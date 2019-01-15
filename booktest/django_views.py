from django.views import View
from django.http import HttpResponse, JsonResponse
import json

from .models import BookInfo


class BooksAPIVIew(View):
    def get(self, request):
        queryset = BookInfo.objects.all()
        book_list = []
        for book in queryset:
            book_list.append({
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'image': book.image.url if book.image else ''
            })
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        json_str_bytes = request.body
        json_str = json_str_bytes.decode()
        print(json_str)
        json_dict = json.loads(json_str)

        # 除了自己的数据可以不用验证,其它人给的所有数据在使用之前必须校验
        # 把数据存储到表中
        book = BookInfo.objects.create(
            btitle=json_dict.get('btitle'),
            bpub_date=json_dict.get('bpub_date')
        )
        # 把模型转换成字典
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bcomment': book.bcomment,
            'bread': book.bread,
            'image': book.image.url if book.image else ''
        }

        # 响应
        return JsonResponse(book_dict, status=201)


class BookAPIView(View):
    def get(self, request, pk):
        """
        获取单个图书信息
        路由： GET  /books/<pk>/
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        })

    def put(self, request, pk):
        json_str_bytes = request.body
        json_str = json_str_bytes.decode()
        json_dict = json.loads(json_str)

        # 获取到要修改的模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'message': 'pk不存在'}, status=404)

        # 修改模型对象
        book.btitle = json_dict['btitle']
        book.bpub_date = json_dict['bpub_date']
        book.bread = json_dict.get('bread', book.bread)
        book.save()

        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bcomment': book.bcomment,
            'bread': book.bread,
            'image': book.image.url if book.image else ''
        }

        # 响应
        return JsonResponse(book_dict, status=200)
    def delete(self, request, pk):
        """
        删除图书
        路由： DELETE /books/<pk>/
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)



