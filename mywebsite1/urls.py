"""
URL configuration for mywebsite1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # Main admin route
    path('register/', include('my_app.urls')),  # Include my_app routes
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login view
    path('', include('my_app.urls')),  # Includes all URLs from my_app
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('my_app.urls')),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
