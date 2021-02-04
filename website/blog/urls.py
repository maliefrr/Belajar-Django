from django.urls import path
from django.conf.urls import handler404
from . import views

app_name = 'MyBlog'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('<int:id>/edit',views.edit,name='edit')

]

handler404 = 'blog.views.handler404'