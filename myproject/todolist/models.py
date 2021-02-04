from django.db import models

# Create your models here.

class Orang(models.Model):
    Nama = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nama


class todolist(models.Model):
    orang = models.ForeignKey(Orang,on_delete=models.CASCADE)
    item = models.CharField(max_length=300)
    condition = models.BooleanField()

    def __str__(self):
        return self.item
