# CodeAlert

A Django-based web application for discovering government, IT jobs, and internships.

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

---

## Deployment on PythonAnywhere (Free Tier)

1. **Sign up** at [pythonanywhere.com](https://www.pythonanywhere.com/).
2. **Upload your code** (via Git or file upload).
3. **Set up a virtual environment:**
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```
6. **Configure the web app** in the PythonAnywhere Web tab:
   - Set the source code path to your project folder.
   - Set the WSGI file path (edit to point to your project's wsgi.py).
7. **Edit the WSGI file** to include:
   ```python
   import sys
   path = '/home/yourusername/yourproject'
   if path not in sys.path:
       sys.path.append(path)
   from CodeAlert.wsgi import application
   ```
8. **Update `CodeAlert/settings.py`:**
   - `DEBUG = False`
   - `ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']`
   - `STATIC_ROOT = '/home/yourusername/yourproject/staticfiles'`
9. **Configure static files** in the Web tab:
   - URL: `/static/` → Directory: `/home/yourusername/yourproject/staticfiles`
10. **Reload the web app** in the Web tab.
11. **Visit** `https://yourusername.pythonanywhere.com/`

---

## License
This project is for educational and demonstration purposes. 