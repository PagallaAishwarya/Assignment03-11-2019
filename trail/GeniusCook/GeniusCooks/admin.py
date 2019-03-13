from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from GeniusCooks.models import Profile,Recipe,Step_Model,Ingredient_Model

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]
# unrigester the old default or inbuild django user model
admin.site.unregister(User)
#registering the new models created
admin.site.register(User,UserAdmin)
admin.site.register(Recipe)
admin.site.register(Step_Model)
admin.site.register(Ingredient_Model)
