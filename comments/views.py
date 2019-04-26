from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.
def post_comment(request, post_pk):
    # get the post that is commented
    # if the post exists, return the post, else return 404
    post = get_object_or_404(Post, pk=post_pk)
    
    # HTTP请求只有get和post两种，一般用户通过表单提交数据都是通过post请求，
    # 因此只有当用户的请求为post时才需要处理表单数据
    if request.method == 'POST':
        # 用户提交的数据存在request.POST中，一个类字典对象
        form = CommentForm(request.POST)
        
        if form.is_valid():  # is_valid方法自动检查表单数据是否符合格式要求
            # save到数据库
            comment = form.save(commit=False)  # 仅保存实例，还不保存评论数据
            # 关联post and comment
            comment.post = post
            
            comment.save()
            # 重定向到post的详情页
            # 当redirect接收一个模型的实例时，会调用这个模型的get_absolute_url()
            # 然后重定向到get_absolute_url返回的URL
            return redirect(post)
        else:   # illegal data, re-render detail page & form error
            
            # get all the comments of current post
            comment_list = post.comment_set.all()  # 等价于 Comment.objects.filter(post=post)
            # 传递三个模板变量给detail.html
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list}
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)   # redirect对HTTP请求重定向，
                            # redirect 可以接受URL作为参数，也可以接受一个模型的实例，如这里的post

