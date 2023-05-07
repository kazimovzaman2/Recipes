# Recipe Django App

Welcome to the Recipe Django App! This application allows users to browse through various recipes, create their own recipes. 

## Features

- Create new recipes
- Edit and delete existing recipes

## Live Demo Website
https://recipe-zaman.azurewebsites.net/

## Installation

1. Clone the repository to your local machine using the following command:
```bash
 git clone https://github.com/your-username/recipe-django-app.git
```
2. Navigate to the project directory:
```bash
cd recipe-django-app
```

3. Create a new virtual environment and activate it:
```bash
virtualenv env
source env/bin/activate
```


4. Install the required packages:
```bash
pip install -r requirements.txt
```

5. Run the server:
```bash
python manage.py runserver
```

6. Navigate to `http://localhost:8000/` in your web browser to access the application.

## Usage

### Creating a Recipe

To create a new recipe, click on the "Create Recipe" button on the homepage. Fill out the form with the recipe title, description, ingredients, and instructions. You can also add a photo of your recipe by clicking on the "Choose File" button. When you're finished, click on the "Create Recipe" button to save your recipe.

### Editing a Recipe

To edit an existing recipe, go to the recipe page and click on the "Edit Recipe" button. Make any desired changes to the recipe and click on the "Save Changes" button to update the recipe.

### Deleting a Recipe

To delete a recipe, go to the recipe page and click on the "Delete Recipe" button. Confirm that you want to delete the recipe by clicking on the "Yes, delete it" button.


The application uses the following resources:

- Django (https://www.djangoproject.com/)
- Bootstrap (https://getbootstrap.com/)
- Font Awesome (https://fontawesome.com/)
