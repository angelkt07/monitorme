from django.shortcuts import render
from core.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def user_profile(request, username):
    user = User.objects.get(username=request.user)
    return render(request, 'core/user_profile.html', {"user":user})

def index(request):
    context = { 
    }
    return render(request, 'index.html', context=context)

def disclosure(request):
    context = {
    }
    return render(request, 'core/disclosure.html', context=context)

def edit_profile(request):
    context = {
    }
    return render(request, 'core/edit_profile.html', context=context)