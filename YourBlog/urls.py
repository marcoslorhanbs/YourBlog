from django.contrib import admin
from django.urls import path
from YourBlogApp.views import Home, CreateAccountPage, CreateBlogPage, createUser, createBlog, editBlogPage
from YourBlogApp.views import YourBlogPage, editBlogTemplate, SignInPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=Home),
    path('accountcreation/', view=CreateAccountPage),
    path('blogcreation/', view=CreateBlogPage),
    path('create-account/', view=createUser),
    path('create-blog/', view=createBlog),
    path('blog-edit/', view=editBlogPage),
    path('yourblog/', view=YourBlogPage),
    path('blogEdit-template/', view=editBlogTemplate),
    path('signIn/', view=SignInPage)
]
