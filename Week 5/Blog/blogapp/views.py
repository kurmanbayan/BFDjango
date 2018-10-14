from django.shortcuts import render, redirect
from .models import Blog, Comment

def blogs(request):
    blogs = Blog.objects.all().order_by('created_at')
    return render(request, 'blog_list.html', {"blogs": blogs})

def comments(request, id):
    blogs = Blog.objects.all().filter(id=id)
    comments = Comment.objects.filter(blog_fk=id)
    context = {
        "blogs": blogs,
        "comments": comments,
        "id": id
    }
    return render(request, 'blog_list.html', context)

def addBlog(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        if request.user.is_authenticated:
            Blog.objects.create(title=title, body=body, user=request.user)
        else:
            Blog.objects.create(title=title, body=body)
    return redirect('blog')

def addComment(request, id):
    if request.method == 'POST':
        blog = Blog.objects.get(id=id)
        if request.user.is_authenticated:
            Comment.objects.create(comment=request.POST['comment'], blog_fk=blog, user=request.user)
        else:
            Comment.objects.create(comment=request.POST['comment'], blog_fk=blog)
    return redirect('comments', id)
