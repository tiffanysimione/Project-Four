from django.contrib import admin

# Register your models here.
from .models import dog, Food
admin.site.register(dog)
admin.site.register(Food)
