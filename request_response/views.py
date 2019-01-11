import json
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render

# Create your views here.


def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')


def get_body_form(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')


def get_body_json(request):
    json_str = request.body
    json_str = json_str.decode()  # python3.6 无需执行此步
    req_data = json.loads(json_str)
    print(req_data)
    return HttpResponse('OK')


def demo_view(request):
    response = HttpResponse('python')
    response.status_code = 400
    response['xixi'] = 'gugu'
    return response


# def first(request):
#     return HttpResponsePermanentRedirect(demo_view)


def demo_json(request):
    return JsonResponse({'city': 'beijing'})


def cookie_set(request):
    response = HttpResponse('ok')
    response.set_cookie('xixi', 'guguji', max_age=60 * 60)
    cookie1 = request.COOKIES.get('xixi')
    print(cookie1)
    return response


def session_set(request):
    request.session['age'] = 'chaoge'
    # 读取
    # 当我们进行设置session时会生成一个sessionid 然后通过response对象设置到cookie并保存到浏览器上
    # 当我们要读取session需要通过请求对象带过来的cookie中的sessionid才能取到这条session记录,再通过age键取到对应的value
    # print(request.session['age'])
    return HttpResponse('session_demo')





