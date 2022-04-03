from flask import Flask, render_template, request, session, redirect
from flask_session import Session
import pymysql, urllib.parse, re
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
conn = pymysql.connect(host="localhost", user="kohack", passwd="KoHack2022", database="kohack2022", autocommit=True)
cursor = conn.cursor(pymysql.cursors.DictCursor)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        uname = request.form.get('name')
        pwd = request.form.get('pwd')
        if not uname or not pwd:
            return render_template('login.html', status='Please enter a valid username and password')
        cursor.execute(f"SELECT * FROM `users` WHERE username = '{uname}'")
        row = cursor.fetchone()
        if not row or row['pwd'] != pwd:
            return render_template('login.html', status='Please enter the correct username and password')
        else:
            session['name'] = row['name']
            return redirect('http://localhost:8080/')
    if not session.get('name'):
        return render_template('login.html', status='')
    else:
        return redirect('http://localhost:8080/')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        uname = request.form.get('uname')
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        if not uname or not name or not pwd:
            return render_template('signup.html', status = 'Please enter a valid username and password')
        if len(uname) < 6 or len(uname) > 32:
            return render_template('signup.html', status = 'Usernames must be between 6 and 32 characters')
        cursor.execute(f"SELECT * FROM `users` WHERE username = '{uname}'")
        row = cursor.fetchone()
        if row:
            return render_template('signup.html', status = 'This username is already in use')        
        if not re.search('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{6,99}', pwd):
            return render_template('signup.html', status = 'Passwords must be between 6 and 99 characters and contain at least one capital letter, one lowercase letter, and one number')
        cursor.execute(f"INSERT INTO `users` (username, name, pwd) VALUES ('{uname}', '{name}', '{pwd}');")
        session['name'] = name
        return redirect('http://localhost:8080/')
    if not session.get('name'):
        return render_template('signup.html', status = '')
    else:
        return redirect('http://localhost:8080/')
@app.route('/clear')
def clear():
    session['name'] = ''
    return redirect('http://localhost:8080/')
app.run("0.0.0.0", port=8080)