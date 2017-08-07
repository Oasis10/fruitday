# coding:utf-8

from django.shortcuts import redirect
from django.http import HttpResponseRedirect, JsonResponse

def log_in(func):
    def login_view(request, *args, **kwargs):
        # 判断session中是否有用户登录信息
        if request.session.has_key('user_id'):
            return func(request, *args, **kwargs)
        else:
            if request.is_ajax():
                return JsonResponse({'is_login':0})
            # 构建重定向响应对象
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_view



