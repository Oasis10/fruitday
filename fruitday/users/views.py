# coding:utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from models import *
import hashlib
from users_decorator import log_in

def index(request):
    return render(request, 'users/index.html', {"title":"首页"})


def register(request):
    # 初步处理注册请求
    context = {"title":"用户注册"}
    return render(request, 'users/register.html', context)

def register_handle(request):
    # 具体处理注册信息
    post = request.POST
    name = post.get('user_name')
    pwd = post.get('pwd')
    print "pwd"+pwd
    cpwd = post.get('cpwd')
    print "cpwd" + cpwd
    email = post.get('email')
    if pwd != cpwd:
        # 判断两次密码是否相同，如果不相同重定向到注册页
        return redirect('/register/')
    user = UserInfo()
    user.name = name
    user.password = hashlib.sha1(pwd).hexdigest()
    print "usr"+user.password
    user.email = email
    user.save()
    return render(request, 'users/register.html', {"title":"注册成功"})

def register_exist(request):
    # 判断用户名是否存在
    name = request.GET.get("uname")
    # count = len(UserInfo.objects.filter(name=name))
    count = UserInfo.objects.filter(name=name).count()
    return JsonResponse({"count":count})

def login(request):
    name = request.COOKIES.get('name', '') # 获取cookie中存储的用户名，如果没有默认为空
    context = {'title':'用户登录', "err_name":0, "err_pwd":0, "name":name}
    return render(request, 'users/login.html', context)

def login_check(request):
    post = request.POST
    name = post.get('username')
    pwd = post.get('pwd')
    print pwd
    pwd_sha1 = hashlib.sha1(pwd).hexdigest()
    print pwd_sha1
    user = UserInfo.objects.filter(name=name) # []
    jizhu = post.get('jizhu', 0) # 查询是否记住用户名，设定默认值0(未记住)
    if len(user) == 1:
        if user[0].password == pwd_sha1:
            url = request.COOKIES.get('url', '/')
            # 查询是url cookie
            red = HttpResponseRedirect(url)
            # 清除cookie
            red.set_cookie('url', '', max_age=-1)
            # 判断是否记住用户名
            if jizhu:
                # 创建cookie
                red.set_cookie('name', name)
            else:
                # 如果不记住立即清除cookie
                red.set_cookie('name', '', max_age=-1)
            request.session['user_id'] = user[0].id
            request.session['name'] = name
            return red
        else:
            context = {"title":"用户登录", "err_name":0, "err_pwd":1, "name":name, "pwd":pwd}
            return render(request, 'users/login.html', context)
    else:
        context = {"title": "用户登录", "err_name": 1, "err_pwd": 0, "name": name, "pwd": pwd}
        return render(request, 'users/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

@log_in
def user_center_info(request):
    return render(request, 'users/user_center_info.html', {"title":"用户中心"})








