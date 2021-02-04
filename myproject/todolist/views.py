from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect
from .models import Orang,todolist
from .forms import Check

# Create your views here.
def index(request):
    orang = Orang.objects.all()
    
    if request.method == 'POST':
        NewUser = request.POST['NewUser']
        Orang.objects.create(Nama=NewUser)
        return HttpResponseRedirect(request.path_info)

    return render(request,'todolist/index.html',{'orang':orang})

def detail(request,id):
    item = get_object_or_404(Orang,pk=id)

    if request.method == 'POST':
        if request.POST.get('NewItem'):
            NewItem = request.POST['NewItem']
            item.todolist_set.create(item=NewItem,condition=False)
            return HttpResponseRedirect(request.path_info)
        elif request.POST.get('Update'):    
            form = Check(request.POST)
                         
    
    return render(request,'todolist/detail.html',{'item':item})
