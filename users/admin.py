from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'gender','language','currency','superhost')
    list_filter = ('language','currency','superhost',)

    fieldsets = UserAdmin.fieldsets + (
        ("Personal",{"fields":("avatar","bio","gender")}),
    )
    