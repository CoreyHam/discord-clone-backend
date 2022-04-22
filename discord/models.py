from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Server(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Channel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Relationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_friend = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    content = models.TextField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content