from flask import Flask, render_template, request, redirect, url_for, session,flash
import random
from flask_mail import Mail, Message
import mysql.connector
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.config['MAIL_SERVER'] = config.MAIL_SERVER
app.config['MAIL_PORT'] = config.MAIL_PORT
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = config.MAIL_USE_TLS
mail = Mail(app)
def get_db_connection():
    conn = mysql.connector.connect(
    host = config.DB_HOST,
     user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
    )
    return conn

@app.route('/')
def home():
    return render_template("index.html")

# ------------------------------------------------------
# ROUTE 1: Show Admin Signup Form
# ------------------------------------------------------
@app.route('/admin-signup', methods=['GET', 'POST'])
def admin_signup():
    if request.method == 'GET':
        return render_template("admin/admin_signup.html")

    name = request.form['name']
    email = request.form['email']

    # 🔍 Check if email already registered
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin WHERE email=%s", (email,))
    existing_admin = cursor.fetchone()
    cursor.close()
    conn.close()

    if existing_admin:
        flash("This email is already registered!", "danger")
        return redirect("/admin-signup")

    # ✔ If email not found → continue OTP process
    session['signup_name'] = name
    session['signup_email'] = email

    otp = random.randint(100000, 999999)
    session['otp'] = otp

    msg = Message("SmartCart Admin OTP", sender=config.MAIL_USERNAME, recipients=[email])
    msg.body = f"Your OTP for SmartCart Admin Registration is: {otp}"
    mail.send(msg)

    flash("OTP sent to your email!", "success")
    return redirect("/verify-otp")
if __name__ == '__main__':
    app.run(debug=True)
