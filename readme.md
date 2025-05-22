# Django Hospital Management System

A comprehensive healthcare platform with user authentication and blog functionality for doctors and patients.

## Features

### Core Authentication System
- **Role-based Signup** for Doctors and Patients
  - Profile Picture upload
  - Address details (line1, city, state, pincode)
- Password confirmation validation
- Separate dashboards for each role
- Admin interface for user management

### Blog System (New!)
- Doctors can:
  - Create blog posts with categories (Mental Health, Heart Disease, etc.)
  - Upload featured images
  - Save as draft or publish
  - View all their posts
- Patients can:
  - Browse published posts
  - Filter by categories
  - View truncated summaries (15 words)

## Technologies Used

- Python 3.x
- Django 5.2.x
- MySQL (Switched from SQLite)
- Pillow (image processing)
- Bootstrap 5 (frontend)

## Installation

```bash
git clone https://github.com/priyanshgitthat/test-assignment.git
cd test-assignment

# Set up virtual environment
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# MySQL Setup
# 1. Create database 'hospital_db'
# 2. Update settings.py with your credentials

# Apply migrations
python manage.py migrate

# Create admin
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## Screenshots
![alt text](<screenshots/Screenshot (108).png>)
![Screenshot (108)](<screenshots/Screenshot (108).png>)  
![Screenshot (109)](<screenshots/Screenshot (109).png>)  
![Screenshot (110)](<screenshots/Screenshot (110).png>)  
![Screenshot (111)](<screenshots/Screenshot (111).png>)  
![Screenshot (112)](<screenshots/Screenshot (112).png>)  
![Screenshot (113)](<screenshots/Screenshot (113).png>)  
![Screenshot (114)](<screenshots/Screenshot (114).png>)  
![Screenshot (115)](<screenshots/Screenshot (115).png>)  
![Screenshot (116)](<screenshots/Screenshot (116).png>)  
![Screenshot (117)](<screenshots/Screenshot (117).png>)



## Usage Guide

### Accounts

        /signup - Create new account

        /login - User login

        /logout - Sign out

### Doctor Features

        /blog/doctor/create - Create new post

        /blog/doctor/blogs - View your posts

### Patient Features

        /blog/patient/blogs - Browse published posts

        ?category=<id> - Filter by category

### Future Enhancements

    Appointment scheduling system

    Doctor-patient messaging

    Blog commenting system

    Advanced search functionality


<section id="contact"> <h2>Contact</h2> <p>Developed by Priyansh</p> <ul> <li>GitHub: <a href="https://github.com/priyanshgitthat" target="_blank">priyanshgitthat</a></li> <li>Email: <a href="mailto:priyanshverma157@gmail.com">priyanshverma157@gmail.com</a></li> <li>LinkedIn: <a href="https://www.linkedin.com/in/priyanshv/" target="_blank">priyanshv</a></li> </ul> </section>