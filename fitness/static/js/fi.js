document.addEventListener("DOMContentLoaded", function () {
    let totalWorkouts = 0;
    let totalCalories = 0;
    let workoutCounts = [3, 5, 7, 8]; // Initial dummy data
    let weeklyCalories = [300, 450, 600, 750];

    // Workout Chart Setup
    const ctx1 = document.getElementById("progressChart").getContext("2d");
    const workoutChart = new Chart(ctx1, {
        type: "bar",
        data: {
            labels: ["Week 1", "Week 2", "Week 3", "Week 4"],
            datasets: [{
                label: "Workouts Completed",
                data: workoutCounts,
                backgroundColor: "rgba(54, 162, 235, 0.6)"
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // Calories Chart Setup
    const ctx2 = document.getElementById("calorieChart").getContext("2d");
    const calorieChart = new Chart(ctx2, {
        type: "line",
        data: {
            labels: ["Week 1", "Week 2", "Week 3", "Week 4"],
            datasets: [{
                label: "Calories Burned",
                data: weeklyCalories,
                borderColor: "rgba(255, 99, 132, 1)",
                backgroundColor: "rgba(255, 99, 132, 0.2)",
                borderWidth: 2,
                fill: true
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // Dynamic Chart Update Functions
    function updateWorkoutChart() {
        workoutChart.data.datasets[0].data = workoutCounts;
        workoutChart.update();
    }

    function updateCalorieChart() {
        calorieChart.data.datasets[0].data = weeklyCalories;
        calorieChart.update();
    }

    function getWeekIndexFromDate(dateStr) {
        const date = new Date(dateStr);
        const day = date.getDate();
    
        if (day <= 7) return 0;       // Week 1
        else if (day <= 14) return 1; // Week 2
        else if (day <= 21) return 2; // Week 3
        else return 3;                // Week 4
    }
    
    function addWorkout(event) {
        event.preventDefault();
        const dateStr = document.getElementById("workout-date").value;
        const weekIndex = getWeekIndexFromDate(dateStr);
    
        workoutCounts[weekIndex]++;
        totalWorkouts++;
        document.getElementById("total-workouts").innerText = totalWorkouts;
    
        updateWorkoutChart();
    }
    
    function addCalories(event) {
        event.preventDefault();
        const dateStr = document.getElementById("calories-date").value;
        const calories = parseInt(document.getElementById("calories-burned").value);
        if (!isNaN(calories) && calories > 0) {
            const weekIndex = getWeekIndexFromDate(dateStr);
            weeklyCalories[weekIndex] += calories;
            totalCalories += calories;
            document.getElementById("total-calories").innerText = totalCalories;
    
            updateCalorieChart();
        } else {
            alert("Please enter a valid calorie amount.");
        }
    }
    

    // BMI Calculation
    function calculateBMI(event) {
        event.preventDefault();
        let weight = parseFloat(document.getElementById("weight").value);
        let height = parseFloat(document.getElementById("height").value);

        if (weight > 0 && height > 0) {
            let bmi = (weight / (height * height)).toFixed(2);
            let resultText = `Your BMI is: ${bmi} - `;

            if (bmi < 18.5) {
                resultText += "Underweight";
            } else if (bmi >= 18.5 && bmi <= 24.9) {
                resultText += "Normal weight";
            } else if (bmi >= 25 && bmi <= 29.9) {
                resultText += "Overweight";
            } else {
                resultText += "Obese";
            }

            document.getElementById("bmi-result").innerText = resultText;
        } else {
            alert("Please enter valid weight and height.");
        }
    }

    // Save Goal
    function saveGoal(event) {
        event.preventDefault();
        const goal = document.getElementById("goal-description").value;
        if (goal) {
            document.getElementById("goal-display").innerText = goal;
        } else {
            alert("Please enter your fitness goal.");
        }
    }

    // Event Listeners
    document.getElementById("workout-form").addEventListener("submit", addWorkout);
    document.getElementById("calories-form").addEventListener("submit", addCalories);
    document.getElementById("bmi-form").addEventListener("submit", calculateBMI);
    document.getElementById("goal-form").addEventListener("submit", saveGoal);
});