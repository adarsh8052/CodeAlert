# CodeAlert

CodeAlert is a web-based job listing and alert system built with Django. It allows users to explore categorized job openings (IT, Government, Internship) with search and filter capabilities. Admins can easily manage job posts using a custom backend. The platform supports rich job descriptions (CKEditor), file uploads, and frontend enhancements for a user-friendly experience.

## Features
- Browse latest IT, government jobs, and internships
- Responsive design for desktop and mobile
- Admin panel for job management
- Rich text editing with CKEditor

---

## Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd CodeAlert
   ```
2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the app:**
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

------------------------------------------------
