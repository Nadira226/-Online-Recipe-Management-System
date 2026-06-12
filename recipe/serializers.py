from rest_framework import serializers
from .models import Category, Recipe, Chef, ChefRecipe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = '__all__'


class ChefRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChefRecipe
        fields = '__all__'