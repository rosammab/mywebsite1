# my_app/urls.py
from django.urls import path
from . import views  # Make sure views is imported
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('admin/', admin.site.urls),  # Admin site URL
    path('register/', views.register, name='register'),  # Register view
    path('profile/', views.profile, name='profile'),  # Profile view
    path('create_post/', views.create_post, name='create_post'),  # Create post view
    path('post/<int:post_id>/comment/', views.comment, name='comment'),  # Comment view
    path('my-posts/', views.user_posts, name='user_posts'),  # User posts view
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),  # Delete post view
    path('home/', views.home, name='home'),  # Home view
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout view
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)