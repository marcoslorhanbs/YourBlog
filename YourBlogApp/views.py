from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from .models import Blog
# Create your views here.
def Home(response):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, response))

def CreateAccountPage(response):
    template = loader.get_template('AccountCreation.html')
    context = {}
    return HttpResponse(template.render(context, response))

def CreateBlogPage(response):
    template = loader.get_template('BlogCreation.html')
    context = {}
    return HttpResponse(template.render(context, response))

def editBlogPage(response):
    template = loader.get_template('BlogEditPage.html')
    context = {}
    return HttpResponse(template.render(context, response))

def YourBlogPage(response):
    template = loader.get_template('yourBlog.html')
    context = {}
    return HttpResponse(template.render(context, response))
def editBlogTemplate(response):
    template = loader.get_template('BlogEditTemplate.html')
    context = {}
    return HttpResponse(template.render(context, response))

def SignInPage(response):
    template = loader.get_template('SignIn.html')
    context = {}
    return HttpResponse(template.render(context, response))

def createUser(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.filter(username=name).first()
       
        if user:
            return HttpResponse('Já existe um usuario com esse username')
        
        createUser = User.objects.create_user(username=name, email=email, password=password)
        createUser.save()
    return HttpResponseRedirect('/blogcreation/')

def createBlog(request):
    if request.method == 'POST':
            blogName = request.POST.get('name')
            blogEmail = request.POST.get('email')
            description = request.POST.get('description')
            #category = request.POST.get('category')
            create_Blog = Blog(name=blogName, email=blogEmail, description=description, category='test')
            create_Blog.save()
    return HttpResponseRedirect('/blog-edit/')