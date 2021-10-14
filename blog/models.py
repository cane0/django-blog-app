from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post_2(models.Model):
    Username = models.CharField(max_length=255)
    Name = models.TextField()
    is_verified = models.CharField(max_length=15)
    is_following = models.CharField(max_length=25)
    page_url = models.TextField()

    def __str__(self):
        return self.Name

