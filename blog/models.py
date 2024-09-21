from django.db import models

# Create your models here.
class Tag(models.Model):
    caption=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name=models.CharField( max_length=50)
    last_name= models.CharField(max_length=50)
    email  =  models.EmailField( max_length=254)
    def __str__(self):
        return f"{self.first_name}"
             

class Post(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(default="",null=True,unique=True)
    date =models.DateField()
    img=models.CharField(null=True,max_length=50)
    excerpt=models.CharField(default="",null=True,max_length=300)
    content=models.TextField(1000)
    author=models.ForeignKey(Author,default="unknown",on_delete=models.SET_DEFAULT)
    tag=models.ManyToManyField(Tag)
    def __str__(self):
        return f"{self.title}"