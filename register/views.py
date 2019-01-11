from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class RegisterView(View):
    """
    类视图：处理注册
    """

    def get(self, request):
        a = request.GET.get('a')
        b = request.GET.get('b')
        print(a,b)
        """

        :param request:处理GET请求
        :return: 返回注册页面
        """
        return render(request, 'register.html')

    def post(self, request):
        return HttpResponse('post')