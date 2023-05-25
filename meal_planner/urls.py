from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_planner, name="meal_planner"),
    path('add_meal/', views.add_meal, name='add_meal'),
    path('ingredient_list/', views.ingredient_list, name='ingredient_list'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('edit_ingredient/<ingredient_id>', views.edit_ingredient, name='edit_ingredient'),
    path('delete_ingredient/<ingredient_id>', views.delete_ingredient, name='delete_ingredient'),
]
