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



