from django.db import models



# Create your models here.

class Tag(models.Model):    
    name=models.CharField(max_length=20,null=True)

    def __str__(self) :
        return self.name

class Project(models.Model):
    CATEGORY=(('Machine Learning','Machine Learning'),
             ('Web Dev','Web Dev'),
             ('Research','Research'))
   
    title = models.CharField(max_length=250)
    descrtion=models.TextField()
    published=models.DateField(auto_now_add=True)
    slug=models.SlugField(unique=True,max_length=100)
    thumb = models.ImageField(blank=True, null=True)
    category=models.CharField(max_length=250,null=True,choices=CATEGORY)
    
    thumb1 = models.ImageField(blank=True, null=True)
    thumb2 = models.ImageField(blank=True, null=True)
    thumb3 = models.ImageField(blank=True, null=True)
    tags=models.ManyToManyField(Tag)
    #add thumbnail
    def __str__(self) :
        return self.title





