# -*- coding:utf-8 -*-
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
from haystack.views import SearchView
from df_cart.models import *

def index(request):
    # 获取所有TypeInfo对象
    type_list = TypeInfo.objects.all()
    # 建立新列表用于存储商品对象
    list = []
    # 遍历所有T对象
    for cur in type_list:
        # 分别获取人气最高商品列表和最新商品列表
        # 人气商品取4个
        click_list = cur.goodsinfo_set.order_by('-click')[0:4]
        # 新品取3个
        new_list = cur.goodsinfo_set.order_by('-id')[0:3]
        # 构造新列表
        list.append({
            'type':cur,
            'click':click_list,
            'new':new_list
        })
    # # 获取cookie
    # all_count = request.COOKIES.get('all_count', 0)
    # 构造context上下文
    context = {'title':'首页', 'list':list, 'cart_count':cart_count(request)}
    print cart_count(request)
    return render(request, 'df_goods/index.html', context)

def goods_list(request, tid, pindex):
    # 获取当前type对象
    cur_type = TypeInfo.objects.get(id=tid)
    # 获取参数
    orderby = request.GET.get('orderby', '')
    # 获取当前type下的所有商品，并依据规则排序
    if orderby == 'n':
        goods_list = cur_type.goodsinfo_set.order_by('-id')
    elif orderby == 'p':
        goods_list = cur_type.goodsinfo_set.order_by('-price')
    elif orderby == 'c':
        goods_list = cur_type.goodsinfo_set.order_by('-click')
    elif orderby == '':
        goods_list = cur_type.goodsinfo_set.order_by('-id')
    # 分页
    paginator = Paginator(goods_list, 10)
    # 获取推荐最新商品
    rec = GoodsInfo.objects.filter(goods_type_id=tid).order_by('-id')[0:2]
    # 判断页码状态
    pindex2 = int(pindex)
    if pindex2 <= 0:
        pindex2 = 1
    elif pindex2 > paginator.num_pages:
        pindex2 = paginator.num_pages
    page_ = paginator.page(pindex2)
    context = {'title':cur_type.title, 'tid':tid, 'page':page_,
               'cur_type':cur_type, 'page1':rec, 'orderby':orderby, 'cart_count':cart_count(request)}
    return render(request, 'df_goods/list.html', context)

def detail(request, gid):
    # 获取当前商品对象
    goods = GoodsInfo.objects.get(id=gid)
    goods.click += 1
    goods.save()
    # 获取cookie
    all_count = request.COOKIES.get('all_count', 0)
    # 新品推荐
    rec = goods.goods_type.goodsinfo_set.order_by('-id')[0:2]
    context = {'title':goods.title, 'goods':goods, 'page1':rec, 'cart_count':cart_count(request)}
    return render(request, 'df_goods/detail.html', context)


def getPage(request, tid):
    ONE_PAGE_OF_DATA = 3
    try:
        cur_page = int(request.GET.get('curPage', '1'))
        all_page = int(request.GET.get('allPage', '1'))
        page_type = str(request.GET.get('pageType', ''))
    except ValueError:
        cur_page = 1
        all_page = 1
        page_type = ''

    # 判断点击了【下一页】还是【上一页】
    if page_type == 'pageDown':
        cur_page += 1
    elif page_type == 'pageUp':
        cur_page -= 1

    # 取出当前页的商品对象
    start_index = (cur_page - 1) * ONE_PAGE_OF_DATA
    end_index = start_index + ONE_PAGE_OF_DATA
    goods_list = GoodsInfo.objects.filter(goods_type_id=tid)
    page = goods_list.order_by('-id')[start_index:end_index]

    # 第一次进入时计算商品总量并分页，之后的数据由GET.get()获得
    if cur_page == 1 and all_page == 1:
        all_counts = goods_list.count()
        all_page = all_counts // ONE_PAGE_OF_DATA
        remain_goods = all_counts % ONE_PAGE_OF_DATA
        if remain_goods > 0:
            all_page += 1
    context = {'title':"商品列表", 'page': page, 'all_page': all_page, 'cur_page': cur_page}
    return render(request, "df_goods/list2.html", context)

class SearchView(SearchView):
    def extra_context(self):
        # 获得查询父类的上下文
        extra = super(SearchView, self).extra_context()
        extra['title'] = self.request.GET.get('q').encode('utf-8') + ' - ' +  '商品搜索'
        extra['cart_count'] = cart_count(self.request)
        return extra

def cart_count(request):
    if request.session.has_key('user_id'):
        all_count = 0
        all_carts = CartInfo.objects.filter(user_id=request.session['user_id'])
        for cart in all_carts:
            all_count += cart.count
        return all_count
    else:
        return 0






