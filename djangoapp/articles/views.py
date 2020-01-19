from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date') #ordering retrived our files by date
    return render(request, "articles/article_list.html",{ 'articles' : articles})
    #specyfing so that django will know which to render 
    #its called namespaceing i think 
    #now we have to register this app
def article_detail(request,slug):
     #return HttpResponse(slug)
     article = Article.objects.get(slug = slug) #quering our database to find the article with given slug
     return render(request,'articles/article_detail.html', { 'article': article})

@login_required(login_url='accounts:login')     #that way if somebody wants to access this page user must be logged in 
def article_create(request):
    if request.method == 'POST':
        #retriving the data
        form = forms.CreateArticle(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid() == True:
            #todo saving the article to the db
            instance =form.save(commit=False) #do not commit just yet that why commit is set to false
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request,'articles/article_create.html', {'form': form})
