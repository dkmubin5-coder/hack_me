from flask import Flask, render_template, request, redirect, session
import sqlite3
import json
import os
import sys

app = Flask(__name__)
app.secret_key = 'your_secret_key123'

# ---- First Setup ----
if "---setup---" in sys.argv:
    if not os.path.exists('mubin.db'):
        conn = sqlite3.connect('mubin.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
        c.execute('''CREATE TABLE posts (id INTEGER PRIMARY KEY, user_id INTEGER, content TEXT)''')
        conn.commit()
        conn.close()
        print("Database and tables created.")
    else:
        print("Database already exists.")
    sys.exit()

    #---- Routes ---- @app.route('/')
    def Facebook_clone():
        if 'user_id' in session:
            return redirect('/home')
        return render_template('Love_HOME_PAGE.html')
    
    @app.route('/auth', methods=['POST'])
    def auth():
        u = request.form['username']
        p = request.form['password']
        t = request.form['type']

        conn = sqlite3.connect('mubin.db')
        c = conn.cursor()
        c. execute("SELECT * FROM users WHERE username=? AND password=?", (u, p, t))
    if result:
        session["user"] = u
        return redirect("/")
    else:
        return "Invalid Love_HOME_PAGE"
    

    @app.route('/home')
    def dash():
        if 'user' not in session:
            return redirect('/')
        return render_template('Love_HOME_PAGE.html', user=session['user'])
    
    app.run(host="0.0.0.0", port=8080)
