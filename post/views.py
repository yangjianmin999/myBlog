# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def get_post_by_num(num):
    # 转换int类型
    num = int(num)
    page_posts=Paginator(Post.objects.order_by("-created"),per_page=5)

    # 判断当前页是否越界
    if num <=0:
        num = 1

    if num >page_posts.num_pages:
        num = page_posts.num_pages

    # 生成页码数
    # 起始数
    start = ((num-1)/10)*10+1

    # 末尾数
    end = start +10

    # 判断end是否越界
    if end > page_posts.num_pages:
        end = page_posts.num_pages+1

    return page_posts.page(num),range(start,end)

def index_view(request,num='1'):
    # 查询第一页的数据
    page_posts,page_range= get_post_by_num(num)
    return render(request,'index.html',{'page_posts':page_posts,'page_range':page_range})

def get_postbyid(postid):
    post =  Post.objects.get(id=postid)
    return post

def post_view(request,postid):
    print postid
    post = get_postbyid(postid)
    return render(request,'detail.html',{'post':post})


def cate_view(request,cateid):
    cates = Post.objects.filter(category_id=int(cateid)).order_by('-created')
    return render(request,'archive.html',{'archive_posts':cates})

#归档功能
def archive_view(request,year=None,month=None):
    if year and month:
        cate_posts = Post.objects.filter(created__year=year,created__month=month).order_by('-created')
    else:
        cate_posts = Post.objects.order_by('-created')

    return render(request, 'archive.html', {'archive_posts': cate_posts})

# 关于
def aboutme_view(request):
    return render(request,'aboutme.html')

# 全文搜索功能
def search_view(request):
    from haystack.query import SearchQuerySet
    from haystack.query import SQ

    # 获取请求参数
    keywords = request.GET.get('q','')
    search_posts = SearchQuerySet().filter(SQ(title=keywords)|SQ(content=keywords))
    s_posts = []

    for s_p in search_posts:
        s_posts.append(s_p.object)

    return render(request,'archive.html',{'archive_posts':s_posts})