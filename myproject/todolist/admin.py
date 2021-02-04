from django.contrib import admin
from .models import Orang,todolist

# Register your models here.

class Todolist(admin.StackedInline):
    model = todolist

class AdminOrang(admin.ModelAdmin):
    inlines = [Todolist,]


admin.site.register(Orang,AdminOrang)       
