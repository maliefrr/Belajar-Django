from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Blog,Comment
from . import forms
# Create your views here.

def handler404(request,exception):
    return render(request,'404.html',status=404)

def index(request):
    blogs = Blog.objects.all()
    return render(request,'blog/index.html',{'blogs':blogs})


def detail(request,id):
    blog = get_object_or_404(Blog,pk=id)
    form = forms.CommentForm()

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            komentar = request.POST['desc']
            blog.comment_set.create(desc=komentar)
            messages.success(request,'Berhasil Submit Komentar')
            return HttpResponseRedirect(request.path_info)

    return render(request,'blog/detail.html',{'blog':blog,'form':form})

# belum berhasil edit 
def edit(request,id):
    komentar = get_object_or_404(Comment,pk=id)
    form = forms.CommentForm(instance=komentar)
    if request.method == 'POST':
        form = forms.CommentForm(instance=komentar,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil Edit Komentar')
            return HttpResponseRedirect(reverse('MyBlog:detail',args=(id,)))

    return render(request,'blog/edit.html',{'komentar':komentar,'form':form})
   
    

