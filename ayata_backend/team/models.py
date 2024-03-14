from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    last_modified_date = models.DateTimeField(auto_now=True,editable=False)
    is_deleted = models.BooleanField(default=False)

class Team(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class User(BaseModel):
    name = models.CharField()
    image = models.ImageField(upload_to=None, null= True, blank= True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_executive = models.BooleanField(default=False)
    description = models.TextField()

class SocialLink(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    type =models.CharField(max_length=255)
    url = models.URLField(max_length=200)

class Works(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class WorkImage(models.Model):
    work = models.ForeignKey(Works, max_length=255, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None) 
