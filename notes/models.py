from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    ref = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    textnote = models.TextField()
    create= models.DateTimeField(auto_now_add=True)
    update= models.DateField(auto_now=True)
    
    def __str__(self):
        return self.textnote

    