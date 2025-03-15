# blogsite/urls.py
from django.contrib.auth.views import LogoutView

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),  # Including blogapp URLs
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.contrib import admin
from django.urls import path
from blogapp import views  # Import your views here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add this line to map the root URL
    path('<int:pk>/', views.post_detail, name='post_detail'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),  # Correctly include blogapp URLs
]
from django.urls import path
from blogapp.views import post_list, post_create


urlpatterns = [
    path('', post_list, name='post_list'),  # Ensure this line exists
    path('post/create/', post_create, name='post_create'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Ensure this line is present
    path('', include('blogapp.urls')),  # Your blog URLs
]
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # The home view should be linked to the root URL
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),  # This links to blogapp's URLs
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),  # ✅ Ensure 'blogapp.urls' is included
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blogapp.urls")),  # ✅ Ensure this line is present
]
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),  # Include blogapp URLs
    path('login/', auth_views.LoginView.as_view(template_name='blogapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='post_list'), name='logout'),


]

from django.contrib.auth import views as auth_views
from django.urls import path
from blogapp import views  # Import your views if needed

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('logout/', views.logout_view, name='logout'),
    
    # Add login URL
    path('login/', auth_views.LoginView.as_view(template_name='blogapp/login.html'), name='login'),
    path('signup/', views.signup_view, name='signup'),
]
from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Home page
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
