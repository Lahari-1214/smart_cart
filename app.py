from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
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
if __name__ == '__main__':
    app.run(debug=True)
