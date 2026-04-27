# Cartify - Full-Stack eCommerce Web Application (Flask)
Cartify is a full-stack eCommerce web application built using the Flask framework.
It simulates a real-world online shopping platform with features like product management, user authentication, cart handling, secure payments, and invoice generation.

### Features

#### Admin Module
+ Admin registration with OTP verification
+ Secure login using hashed passwords (bcrypt)
+ Add, update, delete products
+ Upload and manage product images
+ Search and filter products
+ Update admin profile

#### User Module
+ User registration and login
+ Browse products with images and pricing
+ Search and filter by category
+ View detailed product pages

#### Cart System
+ Add to cart (session-based)
+ Update product quantity
+ Remove items from cart
+ Dynamic total price calculation

#### Payment Integration
+ Razorpay payment gateway integration
+ Secure order creation
+ Payment signature verification
+ Handles successful and failed transactions

#### Invoice Generation
+ Dynamic invoice creation using HTML
+ Convert invoice to PDF (xhtml2pdf / WeasyPrint)
+ Download/view invoice anytime

#### Order Management
+ Store orders in database
+ View order history
+ Maintain order details with product list

#### Additional Features
Flash messages for user feedback
Error handling with try/except
Session management for security
Responsive UI using Bootstrap
Email notifications (OTP / order confirmation)


#### Tech Stack

<strong>>Backend:</strong>

Python (Flask)

<strong>Frontend:</strong>

HTML, CSS, Bootstrap, JavaScript

<strong>Database:</strong>

MySQL / SQLite

<strong>Libraries & Tools:</strong>

Flask
Flask-Mail (OTP)
bcrypt (password hashing)
Razorpay API
xhtml2pdf / WeasyPrint

#### Project structure
<pre>
Cartify/
│
├── app.py
├── config.py
├── requirements.txt
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   ├── uploads/
│
├── templates/
│   ├── base.html
│   ├── admin/
│   ├── user/
│
├── database/
│
└── utils/
    ├── email_otp.py
    ├── payment.py
    └── pdf_generator.py

</pre>

#### Database Schema
Admin
Users
Products
Orders
Order Items
Relational mapping ensures proper order tracking and product management.

#### Installation & Setup
1. Clone the repository
<code>git clone https://github.com/your-username/cartify.git
cd cartify</code>

2. Create virtual environment
<code>python -m venv venv
venv\Scripts\activate   # Windows</code>

3. Install dependencies
<code>pip install -r requirements.txt</code>

4. Configure environment

Update config.py with:

Database credentials
Email configuration
Razorpay API keys

5. Run the application
<code>python app.py</code>

App will run on:
<code>http://127.0.0.1:5000/</code>

#### Security Features
Password hashing using bcrypt
Session-based authentication
OTP verification for admin signup
Payment verification using Razorpay signature

#### Learning Outcomes

This project demonstrates:
Full-stack web development using Flask
Authentication & session management
Database design and relationships
Payment gateway integration
File handling and image upload
PDF generation
Real-world application architecture

#### Screenshots (Optional)

Add screenshots of:

Home page
Admin dashboard
Cart page
Payment screen
Invoice PDF

#### Deployment

This project can be deployed on:

PythonAnywhere
Render
AWS / VPS

#### Author

Leela Kanthi
B.Tech Computer Science
Backend Developer (Flask | Java | SQL)

⭐ Support
If you like this project, give it a ⭐ on GitHub!


