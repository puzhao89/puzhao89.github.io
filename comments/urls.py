# coding=utf-8
# !/usr/bin/env python
# @Project   :    blogproject
# @File name :    urls.py 
# @Author    :    AHUI
# @Contact   :    omegazhanghui@gmail.com
# @Date      :    2019-04-24 11:25
# @SITE      :    https://github.com/Hui9409

from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
        url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment')
    ]

if __name__ == '__main__':
    pass