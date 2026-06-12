from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):

    DIFFICULTY_CHOICES = [('Easy', 'Easy'),('Medium', 'Medium'),('Hard', 'Hard'),]
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='recipes')

    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    steps = models.TextField()
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    difficulty = models.CharField(max_length=10,choices=DIFFICULTY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='recipe_images/',null=True,blank=True)
    recipe_file = models.FileField(upload_to='recipe_files/',null=True,blank=True)

    def __str__(self):
        return self.title


class Chef(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    experience = models.IntegerField()
    profile_photo = models.ImageField(upload_to='chef_profiles/',null=True,blank=True)

    def __str__(self):
        return self.name


class ChefRecipe(models.Model):
    chef = models.ForeignKey(Chef,on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chef.name} - {self.recipe.title}"