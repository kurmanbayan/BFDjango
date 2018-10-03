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
        "comments": comments
    }
    return render(request, 'blog_list.html', context)

def addBlog(request):
    title = request.POST['title']
    body = request.POST['body']
    Blog.objects.create(title=title, body=body)
    return redirect('/api/v1/blog/')
