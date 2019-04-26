# coding=utf-8
# !/usr/bin/env python
# @Project   :    blogproject
# @File name :    urls.py 
# @Author    :    AHUI
# @Contact   :    omegazhanghui@gmail.com
# @Date      :    2019-04-23 16:11
# @SITE      :    https://github.com/Hui9409
'''
不同于blogproject下的urls（整个工程项目的URL配置），这个文件将用于blog引用相关的URL配置
'''
from django.conf.urls import url

from . import views

app_name = 'blog'  # 指定命名空间
urlpatterns = [
    url(r'^$', views.index, name='index'),  # 1. url 以正则表达式表示，这里匹配的是-以空字符串开头且以空字符串结尾的字符
                                            # 2. 绑定URL和视图函数index
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),  # 以post开头，后跟一个至少一位的数字，并且以、符号结尾，如post/1/
                                                                    # [0-9]+表示一或多位数字，(?P<pk>[0-9]+)表示命名组捕获
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category')
]

if __name__ == '__main__':
    pass