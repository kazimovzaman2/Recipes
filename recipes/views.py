from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Recipe, Meal_Type
from .forms import RecipeForm

# Create your views here.

def recipes(request):
    recipes = Recipe.objects.all()

    context = {'recipes': recipes}
    return render(request, 'recipes/recipes.html', context)


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    context = {'recipe': recipe}
    return render(request, 'recipes/single-recipe.html', context)


@login_required(login_url='login')
def createRecipe(request):
    profile = request.user.profile
    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()

            return redirect('recipes')
    
    context = {'form': form}
    return render(request, 'recipes/recipe_form.html', context)


@login_required(login_url='login')
def updateRecipe(request, pk):
    profile = request.user.profile
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save()

            return redirect('recipes')
    
    context = {'form': form, 'recipes': recipe}
    return render(request, 'recipes/recipe_form.html', context)


@login_required(login_url='login')
def deleteRecipe(request, pk):
    profile = request.user.profile
    recipe = Recipe.objects.get(id=pk)

    if request.method == "POST":
        recipe.delete()
        return redirect('recipes')
    context = {'object': recipe}
    return render(request, 'delete_template.html', context)