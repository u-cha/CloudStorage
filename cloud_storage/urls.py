"""
URL configuration for cloud_storage project.

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
from django.urls import include, path

from accounts import views as account_views
from cloud_storage_site import views as site_views

urlpatterns = [
    path('', site_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('register/', account_views.register, name='register'),
    path('logout/', account_views.user_logout, name='custom_logout'),
    path('accounts/', include('django.contrib.auth.urls')),  # Includes login/logout views
]
