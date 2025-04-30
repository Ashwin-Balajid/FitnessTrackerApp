from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    workout_type = models.CharField(max_length=100)  # Changed to match the form field
    date = models.DateField()  # Changed to match the form field
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.workout_type} - {self.date}"

class Calorie(models.Model):
    calories_burned = models.IntegerField()
    date = models.DateField()  # Renamed from 'date' to 'calories_date' to match form
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.calories_burned} calories on {self.date}"

class BMI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    bmi_value = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_calculated = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"BMI for {self.user.username} on {self.date_calculated}"

class Goal(models.Model):
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
