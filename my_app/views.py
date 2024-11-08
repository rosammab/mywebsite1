
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, Post, Comment
from django.contrib.auth.models import User
from .forms import RegistrationForm, PostForm, CommentForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

def homepage(request):
    return render(request, 'homepage.html')

# Login view
def user_login(request):
    if request.method == 'POST':
        # Use get() to avoid MultiValueDictKeyError
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            # Handle the case where the username or password is missing
            return render(request, 'login.html', {'error': 'Please enter both username and password.'})

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')


# Profile management view
@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

# View to create a new post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('profile')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# View to post a comment
@login_required
def comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_page')  # Redirect to user page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
@login_required
def user_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'user_posts.html', {'posts': posts})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('user_posts')
    return render(request, 'confirm_delete.html', {'post': post})


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        contact_number = request.POST['contact_number']
        password = request.POST['password']
        profile_pic = request.FILES.get('profile_pic', None)

        try:
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                # If username exists, send a message to user to choose another username
                return render(request, 'register.html', {'error': 'Username already taken.'})

            # Create the user if username is unique
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.profile_pic = profile_pic  # assuming your User model has profile_pic field
            user.save()

            return redirect('login')  # redirect to login after successful registration

        except IntegrityError as e:
            return render(request, 'register.html', {'error': 'Error occurred, please try again.'})

    return render(request, 'register.html')

def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)  # Get the logged-in user's profile
    return render(request, 'profile.html', {'user_profile': user_profile})
