from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) #giving the post data
        if form.is_valid():
            user =  form.save() #it returns the ruser
            login(request,user) 
            #to do log user in 
            #sending the user if he logged
            return redirect("articles:list")
    else:        
        form = UserCreationForm()
    return render(request,'accounts/signup.html', { 'form':form })
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log the user in 
            user = form.get_user() #accesingthe user djangfo mmethod 
            login(request,user) #logginh the user by django login funciotn 
            if 'next' in request.POST: 
                return  redirect(request.POST.get('next'))
            else:
                return redirect("articles:list")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request) #django knows which user is curenntly logged
        return redirect('articles:list')
    else:
        logout(request)
        return redirect('articles:list')