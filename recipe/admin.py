from django.contrib import admin
from .models import Category, Recipe, Chef, ChefRecipe

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Chef)
admin.site.register(ChefRecipe)
