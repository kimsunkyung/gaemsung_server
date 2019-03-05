from django.db import models
from django.utils import timezone


class User_extrainfo(models.Model):
    genders = (
        ('m', '남자'),
        ('f', '여자')
    )
    User = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices = genders)

    def __str__(self):
        return str(self.pk)

class Search_Image(models.Model):
    User = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    img = models.ImageField(upload_to='uploaded_image')
    location = models.CharField(max_length=200)
    search_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pk)

class Sub_Image(models.Model):
    search_image = models.ForeignKey(Search_Image,on_delete=models.CASCADE)   #질문
    img = models.ImageField(upload_to='uploaded_image')
    url = models.CharField(max_length=200)

    def __str__(self):
        return str(self.pk)