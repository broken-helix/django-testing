from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


class Meals(models.Model):
    meal_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.meal_name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.ingredient_name


#class Measure(models.Model):
#    measure = models.CharField(max_length=50)


#class Unit(models.Model):
#    unit = models.CharField(max_length=25)


#class MealIngredient(models.Model):
#    ingredient_name = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
#    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
#    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)


#class Meal(models.Model):
#    meal_name = models.CharField(max_length=50, null=False, blank=False)
#    ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
#    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
