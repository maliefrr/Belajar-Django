from django.shortcuts import render,redirect
from .forms import RegistrationForms

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistrationForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")    
    else:
        form = RegistrationForms()
        


    return render(request,'register/daftar.html',{'form':form})
