## 🏋️‍♂️ Fitness Tracker App

# 📌 Project Description
The Fitness Tracker is a Django-based web application that helps users track and manage their daily fitness activities, including workouts, calorie intake, BMI calculation, and personal fitness goals. It provides interactive charts and a personalized dashboard for users to monitor their health and progress over time.

# 🚀 Features

# 1. ✅ User Authentication:
      * Sign up, Sign in, and Log out securely.

# 2. 📝 Track Daily Workouts:
      * Log daily workouts with type, duration, and date.
      * Visualize workout trends using bar charts.

# 3. 🍎 Log Daily Calorie Intake:
      * Record daily calorie intake.
      * View calorie trends with real-time charts.

# 4. 🎯 Set and View Fitness Goals
      * Set and display personalized fitness goals.
      * Track goals easily on the dashboard.

# 5. 📊 BMI Calculation Based on Height and Weight
      * Input height and weight to compute BMI.
      * Dynamically update BMI on the dashboard.

# 6. 📈 Interactive Charts for Workout and Calorie Trends (using Chart.js)
      * Clean, user-friendly layout with separate sections for forms and visual charts.

# 🛠️ Tech Stack

* Frontend: HTML, CSS, JavaScript, Chart.js
* Backend: Django (Python)
* Database: MySQL
* Templates: Django Templating Engine
* Authentication: Django's Built-in User System

# 🧪 Models

* Workout: Stores user workouts (type, duration, date).
* Calorie: Stores calorie intake entries.
* BMI: Stores user height, weight, and calculated BMI.
* Goal: Stores user-defined fitness goals.

# 🔧 Installation & Setup

# Step 1: Clone the Repository
git clone https://github.com/Ashwin_Balajid/fitness-tracker.git
cd fitness-tracker

# Step 2: Set Up Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Step 3: Install Requirements
pip install -r requirements.txt

# Step 4: Database Setup
Make sure MySQL is running, then update settings.py with your MySQL credentials.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Then run:
python manage.py makemigrations
python manage.py migrate

# Step 5: Create Superuser (Optional)
python manage.py createsuperuser

# Step 6: Run the Development Server
python manage.py runserver

# 💻 Usage

* Navigate to http://127.0.0.1:8000/
* Sign up for a new account.
* Log workouts, calorie intake, and BMI.
* Set fitness goals.
* Track your progress through dynamic charts on the dashboard.

# 📊 Charts

* Powered by Chart.js for real-time updates.
* Automatically reflects new entries without page reloads.
* Visual feedback for workouts and calorie logs.

# 🔐 Security Notes

* CSRF protection is enabled.
* Passwords stored securely with Django’s hashing.
* Only logged-in users can access the dashboard.


