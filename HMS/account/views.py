from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from hospital.models import * 
from hospital.forms import *
from django.contrib import messages
from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect

from hospital.models import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from hospital.forms import * 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse


# Create your views here.
def user_login(request):
    context={}
    if request.POST:
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            messages.success(request, "password or username is incorrect")
        else:
            context['login_form']=form
            
    else:
        #messages.success(request, "password or username is incorrect")
        form=UserLoginForm(request.POST)
        context['login_form']=form    
        
    return render(request,'account/user_login.html', context)



class user_registration(SuccessMessageMixin, CreateView):
    model = RegisteredPatients
    template_name = 'account/user_registration.html'
    form_class = MyUserForm
    success_url = reverse_lazy('user_login')
    success_message = "Data Added Successfully"
    paginate_by = 2

'''
def user_registration(request):
    context={}
    
    
    if request.POST:
        form = MyUserForm(request.POST)
        if form.is_valid():
          
            form.save()
            return redirect('user_login')
        else:
            context['register_form']=form
            
            
        
    

        
    else:
        form = MyUserForm(request.POST)
        context['register_form']=form

    
    return render(request, 'account/user_registration.html',context)
'''

def user_logout(request):
    logout(request)
    return redirect('user_login')
    return render(request,'account/logout.html')

    
