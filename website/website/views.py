from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from . import forms

def home(request):
    return render(request,'home.html')

def kontak(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            # ngirim email
            send_mail(
                request.POST['Nama'],
                request.POST['Subject'],
                request.POST['Email'],
                ['aliefm1414@gmail.com'],
                fail_silently = False
            )
            # menyelipkan pesan
            messages.success(request,"Email telah berhasil dikirim")
            return HttpResponseRedirect(reverse('kontak'))

    return render(request,'kontak.html',{'form':form})    