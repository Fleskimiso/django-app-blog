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
from django.urls import path, re_path
from . import views

app_name = 'articles' #namespacing our url #remember that to access variables you need to wrtie 'articles:smt'

#url patterns for our articles module app section or whatever it's called

urlpatterns = [
    path(r'', views.article_list , name='list'), #homepage that's only .com\ list url we want to go
    path('create/', views.article_create, name = 'create'),
    path("<slug:slug>/", views.article_detail, name='detail')
    #re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail)
    #we need catch group that we give name slug
    # with regex which going to second argument in article_detail  [\w-]+/ any letter with - sign with /at the end
]