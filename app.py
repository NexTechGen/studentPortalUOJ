from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/student/login")
def student_login():
    return render_template("student/stud_login.html")

@app.route("/lecture/login")
def lecture_login():
    return render_template("lecture/educator_login.html")

@app.route("/admin/login")
def admin_login():
    return render_template("admin/admin_login.html")

if __name__ == '__main__':  
   app.run(debug=True)