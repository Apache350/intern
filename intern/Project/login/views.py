from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .form import RegistrationForm
from django.http import HttpResponseRedirect
def signup(request):
    if request.method=='POST':
        
        form=RegistrationForm(request.POST)
       
        if form.is_valid():
             U=form.cleaned_data['username']
             
             print(U)
             form.save()
             return HttpResponseRedirect('login')
    else:
        form=RegistrationForm()
    return render(request,'home.html' ,{'form':form})


def login(request):
     return render(request,'dashboard.html',{'username':request.user})
    