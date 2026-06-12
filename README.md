# Online Recipe Management System

## Project Description

The Online Recipe Management System is a Django REST Framework project that allows users to manage recipes, categories, and chefs. The system supports recipe images, recipe PDF files, chef profiles, and recipe-chef relationships.

---

## Features

- Manage Categories
- Manage Recipes
- Manage Chefs
- Upload Recipe Images
- Upload Recipe PDF Files
- Upload Chef Profile Photos
- Many-to-Many Relationship using ChefRecipe
- Django ORM Queries
- REST API Endpoints
- Django Admin Panel

---

## Models

### Category

- name
- description
- created_on

### Recipe

- title
- ingredients
- steps
- prep_time
- cook_time
- difficulty
- created_on
- image
- recipe_file
- category

### Chef

- name
- email
- phone
- experience
- profile_photo

### ChefRecipe

- chef
- recipe
- created_date

---

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Git
- GitHub

---

## ORM Queries Implemented

### Filter Queries

- Get all recipes
- Get dessert recipes
- Get recipe by title
- Get recipes created after a date
- Get easy recipes
- Get experienced chefs
- Get recipes where prep time is less than cook time
- Get categories created this month

### Exclude Queries

- Recipes not in Cakes category
- Recipes where difficulty is not Hard
- Exclude a particular chef
- Recipes with images

### Aggregate Queries

- Count recipes in each category
- Count recipes for each chef
- Average cook time
- Maximum prep time
- Total chef experience

### Relationship Queries

- Get recipes by chef
- Get chefs by recipe
- Add recipe to chef
- Remove recipe from chef

---

## API Endpoints

### Recipe APIs

GET

/api/recipes/

/api/desserts/

/api/easy-recipes/

/api/not-cakes/

/api/not-hard/

/api/recipe/<title>/

### Chef APIs

GET

/api/experienced-chefs/

/api/recipes-by-chef/<chef_name>/

/api/chefs-by-recipe/<recipe_title>/

### Statistics APIs

GET

/api/category-count/

/api/chef-count/

/api/average-cook-time/

/api/max-prep-time/

/api/total-experience/

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Nadira226/-Online-Recipe-Management-System.git
```

### Move Into Project Folder

```bash
cd -Online-Recipe-Management-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install django
pip install djangorestframework
pip install pillow
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

## Admin Panel

Open:

http://127.0.0.1:8000/admin/

Login using superuser credentials.

---

## Project Structure

```text
food/
│
├── recipe/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── admin.py
│
├── food/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── README.md
└── requirements.txt
```

Django REST Framework Project

---

## GitHub Repository

https://github.com/Nadira226/-Online-Recipe-Management-System
