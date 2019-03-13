from django.db import models
from django.contrib.auth.models import User
'''
name : Profile
fields: username, email, first_name, last_name
this model is to create profiles for new user
'''
class Profile(models.Model):
    #Using django's default user profile, added new fields given
    username = models.OneToOneField(User, on_delete = models.CASCADE, unique = True)
    email = models.EmailField(max_length = 250, unique = True)
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250,null = True)
    def __str__(self):
        return str(self.username)
'''
name : Recipe
fields: name, profile - from Profile model
this model is to create recipes for different users. one recipe to one user 
'''
class Recipe(models.Model):
    name = models.CharField(max_length = 250, null = False, default = 'other')
    profile = models.OneToOneField(Profile, on_delete = models.CASCADE, unique = True)
    
'''
name : Recipe
fields: step_text, recipe : from Recipe
this model is to create text to recipe. 
'''
class Step_Model(models.Model):
    step_text = models.TextField(null = False)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.step_text)
'''
name : Recipe
fields: text, recipe : from Recipe
this model is to create ingredients for  different recipes. can add one or more ingredients for a recipe.
'''
class Ingredient_Model(models.Model):
    text = models.TextField(null = False)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.text)
