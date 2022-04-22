from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    def __str__(self):
        return self.email 

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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    users = models.ManyToManyField(User, related_name="members")

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    server = models.ForeignKey(Server, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Relationship(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE, null=True, blank=True)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=255, default='pending')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    content = models.TextField()
    parent = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self):
        return self.content