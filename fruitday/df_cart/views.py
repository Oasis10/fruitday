# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from models import *
from users.users_decorator import *
from df_goods.views import cart_count

@log_in
def add(request):
    get = request.GET
    gid = int(get.get('gid'))
    count = int(get.get('count'))
    print request.session['user_id']
    # 查询是否有购物车对象
    carts = CartInfo.objects.filter(goods_id=gid).filter(user_id=request.session['user_id'])
    # 如果没有查到就创建一个新的购物车对象
    # if not carts.count():
    if len(carts) == 0:
        print 111
        cart = CartInfo()
        cart.goods_id = gid
        cart.user_id = request.session['user_id']
        cart.count = count
        cart.save()
    else:
        cart = carts[0]
        cart.count += int(count)
        cart.save()
    context = {
        'count':cart_count(request)
    }
    return JsonResponse(context)

@log_in
def list(request):
    user_id = request.session['user_id']
    cart_list = CartInfo.objects.filter(user_id=user_id)
    context = {
        'title':'购物车',
        'page_name':1,
        'cart_list':cart_list
    }
    return render(request, 'df_cart/cart.html', context)

def count_change(request):
    cart_id = request.GET.get('id')
    count = request.GET.get('count')
    cart = CartInfo.objects.get(id=cart_id)
    cart.count = count
    cart.save()
    return JsonResponse({'count':count})

def delete(request):
    try:
        cart_id = request.GET.get('cart_id')
        print type(cart_id)
        cart = CartInfo.objects.get(id=cart_id)
        cart.delete()
        return JsonResponse({'result':'ok'})
    except Exception,e:
        print e
        return JsonResponse({'result':'failed'})


