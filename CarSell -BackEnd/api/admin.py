from django.contrib import admin
from .models import Brand, Post, Model, UserRequest, Profile, SpecialPost

# Register your models here.
admin.site.register(Brand)
admin.site.register(Post)
admin.site.register(SpecialPost)
admin.site.register(Model)
admin.site.register(UserRequest)
admin.site.register(Profile)