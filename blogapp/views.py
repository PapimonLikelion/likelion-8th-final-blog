from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blog = Blog.objects
    return render(request, 'home.html', {'blogs': blog})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']   
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/'+str(blog.id)) 

def delete(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()
    return redirect('/')

def update(request, blog_id):
    return render(request, 'update.html', {'blog':blog_id})

def update_final(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.title = request.GET['title']   
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()    
    return redirect('/detail/'+str(blog.id)) 
