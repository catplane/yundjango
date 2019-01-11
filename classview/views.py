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