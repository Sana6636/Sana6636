from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Mock user data for demonstration
users = [
    {"username": "user1", "password": "password123"},
    {"username": "user2", "password": "password456"}
]

# Home route (login/register)
@app.route('/')
def index():
    return render_template('index.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and user['password'] == password:
                return redirect(url_for('dashboard'))
        return "Invalid credentials, please try again!"
    return render_template('login.html')

# Register page (for future extension if needed)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Here you would handle user registration, for now we'll just mock it
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        if password == confirm_password:
            # Logic to add user data to a database goes here
            return redirect(url_for('login'))
        else:
            return "Passwords don't match!"
    return render_template('register.html')

# Dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Topics page
@app.route('/topics')
def topics():
    return render_template('topics.html')

# challenge page
@app.route('/challenge')
def challenge():
    return render_template('challenge.html')

# leaderboard page
@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

# easylevel
@app.route('/easylevel')
def leaderboard1():
    return render_template('easy.html')

# emergencylevel
@app.route('/emergencylevel')
def leaderboard2():
    return render_template('emergency.html')


# quiz page
@app.route('/quizzes')
def quiz():
    return render_template('quiz.html')

# rewards page
@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

