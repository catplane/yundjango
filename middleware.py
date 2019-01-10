def my_middleware(get_response):
    print("init is called")
    def middleware(request):
        print("before request")
        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print("after response")
        return response

    return middleware