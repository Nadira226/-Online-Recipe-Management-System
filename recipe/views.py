from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Avg, Max, Sum, F

from .models import Category, Recipe, Chef, ChefRecipe
from .serializers import (
    CategorySerializer,
    RecipeSerializer,
    ChefSerializer,
    ChefRecipeSerializer
)


@api_view(['GET'])
def all_recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def dessert_recipes(request):
    recipes = Recipe.objects.filter(category__name="Desserts")
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recipe_by_title(request, title):
    recipe = Recipe.objects.get(title=title)
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)


@api_view(['GET'])
def easy_recipes(request):
    recipes = Recipe.objects.filter(difficulty="Easy")
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def experienced_chefs(request):
    chefs = Chef.objects.filter(experience__gt=5)
    serializer = ChefSerializer(chefs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def prep_less_than_cook(request):
    recipes = Recipe.objects.filter(prep_time__lt=F('cook_time'))
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recipes_not_cakes(request):
    recipes = Recipe.objects.exclude(category__name="Cakes")
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def difficulty_not_hard(request):
    recipes = Recipe.objects.exclude(difficulty="Hard")
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_recipe_count(request):
    data = Category.objects.annotate(
        total_recipes=Count('recipes')
    ).values('name', 'total_recipes')

    return Response(data)


@api_view(['GET'])
def chef_recipe_count(request):
    data = Chef.objects.annotate(
        total_recipes=Count('chefrecipe')
    ).values('name', 'total_recipes')

    return Response(data)


@api_view(['GET'])
def average_cook_time(request):
    data = Recipe.objects.aggregate(
        avg_cook_time=Avg('cook_time')
    )

    return Response(data)


@api_view(['GET'])
def maximum_prep_time(request):
    data = Recipe.objects.aggregate(
        max_prep_time=Max('prep_time')
    )

    return Response(data)


@api_view(['GET'])
def total_experience(request):
    data = Chef.objects.aggregate(
        total_experience=Sum('experience')
    )

    return Response(data)


@api_view(['GET'])
def recipes_by_chef(request, chef_name):
    recipes = Recipe.objects.filter(
        chefrecipe__chef__name=chef_name
    )

    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def chefs_by_recipe(request, recipe_title):
    chefs = Chef.objects.filter(
        chefrecipe__recipe__title=recipe_title
    )

    serializer = ChefSerializer(chefs, many=True)
    return Response(serializer.data)