"""djangoapp URL Configuration

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
from django.contrib import admin
from django.urls import path , include # function which will include urls from other apps
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views  as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path(r'articles/', include('articles.urls')), #now django knows about our articles urls app and includes them
    path(r'about', views.about ),  #this is for our about page url pattern (that is only about/)
    path(r'', article_views.article_list, name='home' ) #homepage that's only .com\

]

urlpatterns += staticfiles_urlpatterns() # if we are in debug mode it will append our static files
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #setting up phase for uploading files
#specyfing to which url we are uploading and to which dir should the uploaded files go 