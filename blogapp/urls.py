from django.urls import path
from blogapp.views import home, post_detail, post_create  # Import only existing views

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('post/<int:post_id>/', post_detail, name='post_detail'),  # Post details
    path('post/create/', post_create, name='post_create'),  # Create post
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
]
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # The home view should be linked to the root URL
]
from django.urls import path
from .views import home, post_detail  # Import post_detail view

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>/', post_detail, name='post_detail'),  # Dynamic post URL
]

from django.urls import path
from .views import home, post_detail, post_create

urlpatterns = [
    path('', home, name='post_list'),  # ✅ Change 'home' to 'post_list'
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/create/', post_create, name='post_create'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),  # Ensure this line exists
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_create, name='post_create'),  # Check this
]
from django.urls import path
from .views import post_list, post_detail, post_create  # ✅ Ensure post_detail is imported

urlpatterns = [
    path('', post_list, name='post_list'),  # Homepage
    path('post/<int:post_id>/', post_detail, name='post_detail'),  # ✅ Fix this
    path('post/create/', post_create, name='post_create'),  # Post Create
]
from django.urls import path
from .views import home, post_detail, post_create, delete_comment

urlpatterns = [
    path('', home, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/create/', post_create, name='post_create'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),  # URL for deleting a comment
]

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blogapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # FIXED
    path('signup/', views.signup, name='signup'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
from django.urls import path
from .views import post_list, post_detail  # Import your views

urlpatterns = [
    path('', post_list, name='post_list'),  # Make sure this exists
    path('post/<int:id>/', post_detail, name='post_detail'),
]
from django.urls import path
from .views import post_list, post_detail

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),  # Use 'post_id' instead of 'id'
]
from django.urls import path
from .views import post_list, post_detail, post_create  # Import post_create if it's defined

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),  # Add this line if missing
]
from django.urls import path
from .views import logout_view

urlpatterns = [
    path("logout/", logout_view, name="logout"),
]
