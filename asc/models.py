from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    bio = models.TextField()
    status = models.CharField(max_length=100)
    picture = models.ImageField()

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()

    def __str__(self):
        return self.title