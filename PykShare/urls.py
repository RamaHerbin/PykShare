"""PykShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from PykShare import settings
from app import views
from app.views import PostList, PostCreate, AddCommentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', PostList.as_view(), name='feed'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('newpost/', PostCreate.as_view(), name='newpost'),
    path('feed/<int:pk>/newcomment/', AddCommentView.as_view(), name='newcomment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
