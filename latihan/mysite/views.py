from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    user = User
    return render(request,'mysite/index.html',{'user':user})
    
