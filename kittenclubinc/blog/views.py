from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger

def post_list(request):
    post_list = Post.published.all()
    # Разбивка 3 постами в одну страницу
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        #if page=char_value
        posts=paginator.page(1)


    return render(request,
                  'blog/post/list.html',
                  {'posts':posts})

def post_detail(request, year, month, day, post):
    post=get_object_or_404(Post,
                           status=Post.Status.PUBLISHED,
                           slug=post,
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post':post})

# from django.shortcuts import render, get_object_or_404
# from .models import Post
#
#
# def post_list(request):
#     posts = Post.published.all()
#     return render(request,
#                  'blog/post/list.html',
#                  {'posts': posts})
#
#
# def post_detail(request, id):
#     post = get_object_or_404(Post,
#                              id=id,
#                              status=Post.Status.PUBLISHED)
#     return render(request,
#                   'blog/post/detail.html',
#                   {'post': post})