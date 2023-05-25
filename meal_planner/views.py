from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient, Meals
from .forms import IngredientForm, MealForm


# Create your views here.
def meal_planner(request):
    meals = Meals.objects.all()
    context = {
        'meals': meals
    }
    return render(request, 'meal_planner.html', context)


def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_meal.html',)
    form = MealForm()
    context = {
        'form': form
    }
    return render(request, 'add_meal.html', context)


def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    context = {
        'ingredients': ingredients
    }
    return render(request, 'ingredient_list.html', context)


def add_ingredient(request):
    if request.method == 'POST':
        # ingredient_name = request.POST.get('ingredient_name')
        # Ingredient.objects.create(ingredient_name=ingredient_name)
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    form = IngredientForm()
    context = {
        'form': form
    }
    return render(request, 'add_ingredient.html', context)


def edit_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    if request.method == 'POST':
        # ingredient_name = request.POST.get('ingredient_name')
        # Ingredient.objects.create(ingredient_name=ingredient_name)
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    form = IngredientForm(instance=ingredient)
    context = {
        'form': form
    }
    return render(request, 'edit_ingredient.html', context)


def delete_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    ingredient.delete()
    return redirect('ingredient_list')
