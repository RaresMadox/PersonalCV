from django.db import models
from django.contrib.auth.models import User, UserManager
# Create your models here.


class Visit(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name=models.CharField(default="Update your name",max_length=200,null=True)
    firstname=models.CharField(default="Update your first name",max_length=200,null=True)
    lastname=models.CharField(default="Update your last name",max_length=200,null=True)
    phone=models.CharField(default="Update your phone number",max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_create=models.DateTimeField(auto_now_add=True,null=True)
    profile_pic=models.ImageField(default='default_profile.png',null=True,blank=True)

    # def save(self, *args, **kwargs):
    #     # delete old file when replacing by updating the file
    #     try:
    #         this = Visit.objects.get(id=self.id)
    #         if this.profile_pic != self.image:
    #             this.profile_pic.delete(save=False)
    #     except: pass # when new photo then we do nothing, normal case          
    #     super(Visit, self).save(*args, **kwargs)
    objects=UserManager()
    def __str__(self):
        return self.name



