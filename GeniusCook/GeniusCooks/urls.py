from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Recipes',views.RecipeView)
router.register('Recipes/search/',views.RecipeSearchView)

#router.register('Recipes/<string:pk>/',views.RecipeDelView)
#router.register('Recipes/<string:pk>/',views.RecipeView)

urlpatterns = [
    path('',include(router.urls)),
    url(r'Recipes/?<profile>[\w-]+/$',views.RecipeDelView,name ='delete'),
    url(r'Recipes/?<profile>[\w-]+/$',views.RecipeView,name = 'update')
]
