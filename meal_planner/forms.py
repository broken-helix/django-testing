from django import forms
from .models import Ingredient, Meals


class MealForm(forms.ModelForm):
    class Meta:
        model = Meals
        fields = ['meal_name',]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name',]