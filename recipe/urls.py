from django.urls import path
from . import views

urlpatterns = [

    path('recipes/', views.all_recipes),

    path('desserts/', views.dessert_recipes),

    path('recipe/<str:title>/', views.recipe_by_title),

    path('easy-recipes/', views.easy_recipes),

    path('experienced-chefs/', views.experienced_chefs),

    path('prep-less-cook/', views.prep_less_than_cook),

    path('not-cakes/', views.recipes_not_cakes),

    path('not-hard/', views.difficulty_not_hard),

    path('category-count/', views.category_recipe_count),

    path('chef-count/', views.chef_recipe_count),

    path('average-cook-time/', views.average_cook_time),

    path('max-prep-time/', views.maximum_prep_time),

    path('total-experience/', views.total_experience),

    path('recipes-by-chef/<str:chef_name>/', views.recipes_by_chef),

    path('chefs-by-recipe/<str:recipe_title>/', views.chefs_by_recipe),
]