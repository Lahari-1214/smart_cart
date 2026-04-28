# app.py
# ------------------------------------------------------
# Day 1: Basic Flask Setup + MySQL Database Connection
# ------------------------------------------------------

from flask import Flask, render_template
import mysql.connector
import config  # import settings from config.py

app = Flask(__name__)
# Set secret key for session management
app.secret_key = config.SECRET_KEY

# -------------------------------
# MySQL Database Connection Setup
# -------------------------------
def get_db_connection():
    """
    This function creates and returns 
    a connection to the MySQL database.
    We will use this function whenever
    we need to interact with the DB.
    """

    conn = mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )
    return conn

# Home Route (First Flask Route)
# --------------------------------
@app.route('/')
def home():
    return render_template("index.html")


# -------------------------------
# Run the Flask app
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)
