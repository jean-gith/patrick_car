"""projet_location URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mycarapp.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('voiture/',voiture,name="voiture"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('detail/',detail,name="detail"),
    path('reservation/<int:iden>',reservation,name="reservation"),
    path('login_1/',login_1,name="login_1"),
    path('register/',register,name="register"),
    path('logout1/',logout1,name="logout1"),
    path('account/',account,name="account"),
    path('VoitureDetails/<int:logotype>',voiture_details,name="voiture_details"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
