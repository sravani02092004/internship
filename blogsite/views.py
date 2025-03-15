from django.shortcuts import render
  # Import Post model
from blogapp.models import Post  # Correct

def home(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/home.html', {'posts': posts})  # Correct template path
def post_list(request):
    return render(request, "home.html")  # Adjust template name if needed
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),  # Include blogapp URLs
]


