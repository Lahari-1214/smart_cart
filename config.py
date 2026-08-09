# config.py
# ------------------------------------
# This file holds all configurations
# like Secret Key, Database connection
# details, Email settings, Razorpay keys etc.
# ------------------------------------

SECRET_KEY = "your_secret_key_here"   # used for sessions

# MySQL Database Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "leela@123"  # keep empty if no password
DB_NAME = "smartcart_db"


# Email SMTP Configuration (Using Gmail)
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'leelanarayan1214@gmail.com'      # sender email
MAIL_PASSWORD = 'qciu jhss megm heyk'    # Gmail App Password



RAZORPAY_KEY_ID = "rzp_test_RjUGK6hO0z5ZU9"
RAZORPAY_KEY_SECRET = "BpaLXGCGbqqFJtjJETnv7a37"


# rzp_test_RjUGK6hO0z5ZU9,   rzp_test_RjU3xQko7gVLBx
# BpaLXGCGbqqFJtjJETnv7a37,         qRNqA9Ac4Vmr54ZJKuZoDzWi