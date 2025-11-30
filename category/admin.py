from django.contrib import admin
from .models import Category
# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category_name','slug','description','cat_image']

    prepopulated_fields = {'slug':('category_name',)}
