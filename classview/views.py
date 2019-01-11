from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View


def my_decorator(func):
    print('init')
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)
    return wrapper


# 为全部请求方法添加装饰器
#@method_decorator(my_decorator, name='dispatch')
class DemoView(View):
    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    @method_decorator(my_decorator)
    def post(self, request):
        print('post方法')
        return HttpResponse('ok')

    def put(self, request):
        print('put方法')
        return HttpResponse('ok')


class ListModelMixin(object):

    def list(self, request, *args, **kwargs):
        return HttpResponse('ok1')


class CreateModelMixin(object):
    def create(self, request, *args, **kwargs):
        return HttpResponse('ok2')


class BooksView(CreateModelMixin, ListModelMixin, View):
    """
    同时继承两个扩展类，复用list和create方法
    """
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


