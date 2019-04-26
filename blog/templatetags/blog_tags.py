# coding=utf-8
# !/usr/bin/env python
# @Project   :    blogproject
# @File name :    blog_tags.py.py 
# @Author    :    AHUI
# @Contact   :    omegazhanghui@gmail.com
# @Date      :    2019-04-24 09:38
# @SITE      :    https://github.com/Hui9409

from ..models import Post, Category
from django import template

register = template.Library()


@register.simple_tag  # 注册这个函数为模板标签{% get_recent_posts %}
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    '''
    'month' is precision
    :return: dates() returns a list: [p1_created_time, ...]
    '''
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()



