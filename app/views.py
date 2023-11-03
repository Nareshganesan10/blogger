from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from app.models import BlogModel, CommentModel
from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):
    blog_list = BlogModel.objects.all()
    return render(request, 'index.html', {
        'blog_list': blog_list,
    })

@api_view(['POST'])
def post_blog(request):
    if request.method == 'POST':
        blog_content = request.POST.get('blog_content')
        if blog_content is not None:
            blog = BlogModel.objects.create(blog_content=blog_content)
            blog.save()
            return redirect('index')

@ensure_csrf_cookie
@api_view(['POST'])
def post_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        if comment is not None:
            blog = BlogModel.objects.get(id=id)
            post_comment = CommentModel.objects.create(blog_id=blog, comment=comment)
            post_comment.save()
            return redirect('index')
    return render('index')
