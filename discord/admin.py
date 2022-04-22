from django.contrib import admin
from .models import Category, Server, Channel, Relationship, Message
# Register your models here.
admin.site.register(Category)
admin.site.register(Server)
admin.site.register(Channel)
admin.site.register(Relationship)
admin.site.register(Message)