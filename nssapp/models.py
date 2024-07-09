from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER ={
        (1,'admin'),
        (2,'nsuser'),
        
    }
    user_type = models.CharField(choices=USER,max_length=50,default=1)

    profile_pic = models.ImageField(upload_to='media/profile_pic')


class UserReg(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    mobilenumber = models.CharField(max_length=11)
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.admin:
            return f"{self.admin.first_name} {self.admin.last_name} - {self.mobilenumber}"
        else:
            return f"User not associated - {self.mobilenumber}"


class Notes(models.Model):
    nsuser = models.ForeignKey(UserReg, on_delete=models.CASCADE, null=True, blank=True, related_name='notes')
    notestitle = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    notesdesc = models.TextField()
    file1 = models.FileField(upload_to='media/notes/files', null=True, blank=True)
    file2 = models.FileField(upload_to='media/notes/files', null=True, blank=True)
    file3 = models.FileField(upload_to='media/notes/files', null=True, blank=True)
    file4 = models.FileField(upload_to='media/notes/files', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
