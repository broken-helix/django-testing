from django.contrib import admin
from .models import Ingredient, Meals
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Meals)