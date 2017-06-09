# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from models import *
from users.models import *
from users.users_decorator import *
from datetime import datetime
from django.db import transaction
from df_cart.models import *

#
# 1、判断库存
# 2、减少库存
# 3、创建订单对象
# 4、创建详单对象
# 5、删除购物车
# 对于以上操作，应该使用事务
# 问题是：在django的模型类中如何使用事务？
#
# 未实现功能：
#     真实支付
#     物流跟踪
#

@log_in
def order(request):
    post = request.POST
    address = post.get('address')
    print address
    cart_id_list = post.getlist('cart_id')
    print cart_id_list
    # 事务保存点
    sid = transaction.savepoint()
    try:
        # 创建订单对象
        order = OrderInfo()
        now = datetime.now()
        uid = request.session['user_id']
        order.oid = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), uid)
        order.user_id = uid
        order.address = address
        order.total = 0
        order.save()
        # 总金额
        total = 0
        for cart_id in cart_id_list:
            # 获取购物车对象
            cart = CartInfo.objects.get(id=cart_id)
            # 判断库存是否大于购买量
            if cart.goods.inventory >= cart.count:
                # 写入详单对象中
                detail = OrderDetailInfo()
                detail.order = order
                detail.goods = cart.goods
                detail.price = cart.goods.price
                detail.count = cart.count
                detail.save()
                total += cart.goods.price*cart.count
                # 删除购物车数据
                cart.delete()
            else:
                # 库存不足
                transaction.savepoint_rollback(sid)
                return redirect('/cart/')
        # 保存总价
        order.total = total
        order.save()
        transaction.savepoint_commit(sid)
        return redirect('/user/order/')
    except Exception, e:
        print e
        transaction.savepoint_rollback(sid)
        return redirect('/')


