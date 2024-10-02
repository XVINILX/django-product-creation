from django.contrib import admin

from .models import User, Product

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "createdAt", "updatedAt")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("name", "price", "createdAt", "updatedAt")