from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Recipes',views.RecipeView)
router.register('Recipes/<string:pk>/',views.RecipeDelView)
router.register('Recipes/<string:pk>/',views.RecipeView)

urlpatterns = [
    path('',include(router.urls))
]
