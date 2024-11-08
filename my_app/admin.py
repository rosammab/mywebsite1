# admin.py
from django.contrib import admin
from .models import UserProfile, Post, Comment

# Register the UserProfile model
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'contact_number', 'profile_picture')

admin.site.register(UserProfile, UserProfileAdmin)

# Register the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'is_blocked')
    list_filter = ('created_at', 'is_blocked')  # Add filtering options
    search_fields = ('title', 'content')  # Enable search for title and content

admin.site.register(Post, PostAdmin)

# Register the Comment model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('content',)

admin.site.register(Comment, CommentAdmin)
