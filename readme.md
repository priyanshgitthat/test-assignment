# Django Hospital User Signup & Login System

This Django project implements a user authentication system supporting two types of users: **Doctor** and **Patient**. Each user can sign up with extended profile details and is redirected to their respective dashboard upon login.

---

## Features

- Signup for Doctors and Patients with additional profile info:
  - Profile Picture upload
  - Address details (line1, city, state, pincode)
- Password confirmation validation during signup
- Separate dashboards for Doctors and Patients showing their profile details
- User authentication with login and logout
- Admin interface to manage users and profiles

---

## Technologies Used

- Python 3.x
- Django 5.2.x
- SQLite (default Django database)
- Pillow (for handling profile picture uploads)
- Bootstrap 5 (for front-end styling)

---

## Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/priyanshgitthat/test-assignment.git
cd test-assignment
```

## Create and activate a virtual environment:
```
python -m venv env
```
# Windows
```
env\Scripts\activate
```
# macOS/Linux
```
source env/bin/activate

Install dependencies:

pip install -r requirements.txt
```

### (If requirements.txt is not present, install Django and Pillow manually)

### Apply migrations:

```
python manage.py makemigrations
python manage.py migrate
```

## Create a superuser (admin):

```
python manage.py createsuperuser
```

## Run the development server:
```
python manage.py runserver
```

## Open your browser and visit:
```
    http://127.0.0.1:8000/
```

## Usage

###    Navigate to /signup to create a new account (Doctor or Patient)

###    Login via /login

###    After login, you will be redirected to your respective dashboard:
-     /doctor/dashboard/

-      /patient/dashboard/


## Notes
    Profile pictures are stored in the media/profiles folder.

    Make sure to configure MEDIA_URL and MEDIA_ROOT in settings.py for media handling.

    The project uses Bootstrap 5 for responsive and clean UI.

## Future Enhancements

    Add password reset functionality

    Email verification on signup

    User profile update pages

    Better dashboard UI and role-based permissions

<section id="contact">
  <h2>Contact</h2>
  <p>Created by Priyansh</p>
  <ul>
    <li>GitHub: <a href="https://github.com/priyanshgitthat" target="_blank" rel="noopener noreferrer">https://github.com/priyanshgitthat</a></li>
    <li>Email: <a href="mailto:priyanshverma157@gmail.com">priyanshverma157@gmail.com</a></li>
    <li>LinkedIn: <a href="https://www.linkedin.com/in/priyanshv/" target="_blank" rel="noopener noreferrer">https://www.linkedin.com/in/priyanshv/</a></li>
  </ul>
</section>
