# config.py
# ------------------------------------
# This file holds all configurations
# like Secret Key, Database connection
# details, Email settings, Razorpay keys etc.
# ------------------------------------

SECRET_KEY = "123"   # used for sessions
# MySQL Database Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "leela@123"  # keep empty if no password
DB_NAME = "smartcart_db"


# Email SMTP Settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'leelanarayan1214@gmail.com'
MAIL_PASSWORD = 'your_app_password'

