from django.contrib import admin
from django.urls import path
from YourBlogApp.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home)
]
