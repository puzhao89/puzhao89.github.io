import markdown
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from .models import Post, Category

# Create your views here.

# 1. 将HTTP请求传进去
# 2. render根据参数'blog/index.html' 找到模板文件，并读取模板内容
# 3. render根据传入context的参数替换模板中的值
# def index(request):
#     return render(request, 'blog/index.html', context={
#         'title': 'My blog pages',
#         'welcome': 'Welcome to my pages!'
#         })





def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra',       # 使模板中的{{post.body}}显示Markdown渲染后的HTML文本
                                                         'markdown.extensions.codehilite',   # extensions是对Markdown语法的扩展, codehilite = code hilight
                                                        'markdown.extensions.toc'])
    # add comments view in detail pages
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list}
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})
