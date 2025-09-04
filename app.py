from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}
admin_users = set()
student_users = set()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student')
def student_page():
    return render_template('student.html')

@app.route('/admin')
def admin_page():
    return render_template('admin.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            if username in admin_users:
                return render_template('admin.html')
            return render_template('student.html')
        else:
            return "Invalid credentials, please try again.", 400
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['stateSelect']  # admin or student

        if username in users:
            return "Username already taken, please choose another.", 400

        if role == "admin":
            admin_users.add(username)
        else:
            student_users.add(username)

        users[username] = password
        return redirect(url_for('login'))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
