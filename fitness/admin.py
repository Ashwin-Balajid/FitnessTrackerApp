from django.contrib import admin
from .models import Workout, Calorie, BMI, Goal

admin.site.register(Workout)
admin.site.register(Calorie)
admin.site.register(BMI)
admin.site.register(Goal)

