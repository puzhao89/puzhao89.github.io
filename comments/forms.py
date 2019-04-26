# coding=utf-8
# !/usr/bin/env python
# @Project   :    blogproject
# @File name :    forms.py 
# @Author    :    AHUI
# @Contact   :    omegazhanghui@gmail.com
# @Date      :    2019-04-24 10:43
# @SITE      :    https://github.com/Hui9409

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']  # 指定表单需要显示的字段


if __name__ == '__main__':
    pass