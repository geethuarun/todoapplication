from django.db import models

# Create your models here.

class Todos(models.Model):
    title=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    due_date=models.DateField(null=True)


    def __str__(self):
        return self.title
    
class Book(models.Model):
    name=models.CharField(max_length=200,unique=True)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    publisher=models.CharField(max_length=200)

    def __str__(self):
        return self.name 

