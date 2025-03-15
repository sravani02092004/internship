from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Post, Comment
from .forms import SignupForm  # Ensure this import is correct

# Home Page - List of Posts
def home(request):
    posts = Post.objects.all().order_by('-date_posted')  # Show latest posts first
    return render(request, 'blogapp/home.html', {'posts': posts})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

# View Post Details + Handle Comments
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        author = request.POST.get("author")
        text = request.POST.get("text")
        if author and text:
            Comment.objects.create(post=post, author=author, text=text)
            return redirect('post_detail', post_id=post.id)  # Refresh page after comment submission

    return render(request, 'blogapp/post-details.html', {'post': post, 'comments': comments})

# Create a Post (Ensure post_create.html exists)
def post_create(request):
    return render(request, 'blogapp/post_create.html')

# Delete a Comment (Improved)
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.pk  # Store post_id before deleting
    comment.delete()
    return redirect('post_detail', post_id=post_id)  # Redirect safely

# User Signup
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'blogapp/signup.html', {'form': form})

# User Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "blogapp/login.html", {"form": form})

# User Logout
def logout_view(request):
    logout(request)
    return redirect("home")  # Ensure home is defined in your URLs

# Post List
def post_list(request):
    posts = Post.objects.all().order_by('-date_posted')  # Get all posts
    return render(request, "blogapp/home.html", {'posts': posts})  # ✅ Pass posts

# Signup Form Class
from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, post_id):  
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogapp/post-details.html', {'post': post})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/home.html', {'posts': posts})
from django.shortcuts import render

def post_create(request):
    return render(request, 'blogapp/post-create.html')
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'blogapp/signup.html', {'form': form})
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('post_list')  # Redirect to the home page after logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')  # Redirect to home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, "Account created successfully! Please log in.")
                return redirect("login")  # Redirect to login page
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, "blogapp/signup.html")
from django.contrib.auth import logout
from django.shortcuts import redirect
def logout_view(request):
    logout(request)
    return redirect("post_list")  # Redirect to home after logout rome duplicates give my code  out errors omly not remove any other give my alal vcode 