from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import WorkoutForm, CalorieForm, BMIForm, GoalForm
from .models import Workout, Calorie, BMI , Goal
from django.db.models import Count, Sum
from django.core.serializers.json import DjangoJSONEncoder
import json

# 1. Landing Page
def landing_view(request):
    return render(request, 'fitness/landing.html')

# 2. Sign Up

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        print("POST request received.")
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("Username already exists.")
                return render(request, "fitness/signup.html", {"error": "Username already taken"})
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            print("User created successfully. Redirecting to signin.")
            return redirect("signin")
        else:
            print("Passwords do not match.")
            return render(request, "fitness/signup.html", {"error": "Passwords do not match"})

    print("GET request, showing signup form.")
    return render(request, "fitness/signup.html")



# 3. Sign In
def signin_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "fitness/signin.html", {"error": "Invalid username or password"})    
        
    return render(request, 'fitness/signin.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('landing')


@login_required
def dashboard_view(request):
    workout_form = WorkoutForm()
    calorie_form = CalorieForm()
    bmi_form = BMIForm()
    goal_form = GoalForm()

    total_workouts = Workout.objects.filter(user=request.user).count()
    total_calories = Calorie.objects.filter(user=request.user).aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0
    user_goal = Goal.objects.filter(user=request.user).first()

    # Fetch workout data for chart (date and workout count)
    workout_data = list(Workout.objects.filter(user=request.user)
                        .values('date')
                        .annotate(count=Count('id'))
                        .order_by('date'))

    # Fetch calorie data for chart (date and total calories burned)
    calorie_data = list(Calorie.objects.filter(user=request.user)
                        .values('date')
                        .annotate(total=Sum('calories_burned'))
                        .order_by('date'))

    if request.method == 'POST':
        if 'workout_submit' in request.POST:
            workout_form = WorkoutForm(request.POST)
            if workout_form.is_valid():
                workout_instance = workout_form.save(commit=False)
                workout_instance.user = request.user
                workout_instance.save()
                return redirect('dashboard')
            
        elif 'calorie_submit' in request.POST:
            calorie_form = CalorieForm(request.POST)
            if calorie_form.is_valid():
                calorie_instance = calorie_form.save(commit=False)
                calorie_instance.user = request.user
                calorie_instance.save()
                return redirect('dashboard')

        elif 'bmi_submit' in request.POST:
            bmi_form = BMIForm(request.POST)
            if bmi_form.is_valid():
                bmi_instance = bmi_form.save(commit=False)
                bmi_instance.user = request.user
                bmi_instance.bmi_value = bmi_instance.weight / (bmi_instance.height ** 2)
                bmi_instance.save()
                return redirect('dashboard')

        elif 'goal_submit' in request.POST:
            goal_description = request.POST.get('goal_description', '').strip()
            if goal_description:
                goal_instance, created = Goal.objects.get_or_create(user=request.user)
                goal_instance.description = goal_description
                goal_instance.save()
                return redirect('dashboard')

                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return HttpResponse('Goal saved successfully.')
                

    context = {
        'workout_form': workout_form,
        'calorie_form': calorie_form,
        'bmi_form': bmi_form,
        'goal_form': goal_form,
        'total_workouts': total_workouts,
        'total_calories': total_calories,
        'user_goal': user_goal.description if user_goal else 'None',
        'workout_chart_data': json.dumps(workout_data, cls=DjangoJSONEncoder),
        'calorie_chart_data': json.dumps(calorie_data, cls=DjangoJSONEncoder),
    }

    return render(request, 'fitness/fi.html', context)