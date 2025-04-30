from django import forms
from .models import Workout, Calorie, BMI, Goal

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['workout_type', 'date']

class CalorieForm(forms.ModelForm):
    class Meta:
        model = Calorie
        fields = ['calories_burned', 'date']

class BMIForm(forms.ModelForm):
    class Meta:
        model = BMI
        fields = ['weight', 'height']
        widgets = {
            'weight': forms.NumberInput(attrs={'id': 'weight'}),
            'height': forms.NumberInput(attrs={'id': 'height'}),
        }

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['description']
