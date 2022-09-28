from django.db import models
from datetime import date
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
 
class Tag (models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="post", default="placeholder.png")
    state = models.BooleanField('Active',default=False)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    fecha= models.DateField(blank=True, null=True, default=date.today())
    

    def __str__(self):
	    return self.title


class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)




    






      



