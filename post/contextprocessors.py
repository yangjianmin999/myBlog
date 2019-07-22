# coding=utf-8
from models import *

def getrightinfo(request):
    # 分类信息
    from django.db.models import Count
    cate_posts = Post.objects.values('category__cname','category').annotate(count=Count('*')).order_by('-count')

    # 归档信息
    from django.db import connection
    cursor=connection.cursor()
    arc_posts = cursor.execute("select created,count('*') as count from t_post group by strftime('%Y-%m',created) order by count desc")

    # 近期文章
    recent_posts = Post.objects.order_by('-id')[:3]

    return {'cate_posts':cate_posts,'recent_posts':recent_posts,'arc_posts':arc_posts}











