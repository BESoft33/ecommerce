from django.contrib import admin

# Register your models here.
from .models import Category, Brand, Item, User

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Item)
admin.site.register(User)