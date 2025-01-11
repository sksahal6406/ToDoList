from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="todolist",null=True)
    name=models.CharField( max_length=50)
    
    def __str__(self):
        return self.name
    
    
class items(models.Model):
    todolist=models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text=models.CharField(null=True, max_length=500)
    complete=models.BooleanField()
    
    def __str__(self):
        return self.text
    