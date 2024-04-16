from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User  = get_user_model()

class Job(models.Model):
    title = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='media', null=True, blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class SaveJob(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')
    # This means that a user cannot save the same job multiple times.

    def __str__(self):
        return self.user
    

    

class Application(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    experience = models.CharField(max_length=20)
    resume = models.FileField(upload_to='CVs/')

    def __str__(self):
        return self.fullname
