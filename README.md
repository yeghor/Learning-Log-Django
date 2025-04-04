# Learning Log Django Project

This is web application written in Django, that allows users to keep track on their learning progress.

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yeghor/Learning-Log-Django.git
cd Learning-Log-Django
```
2. **Create a virtual enviroment:**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate
```

3. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up the database:**
```bash
python manage.py migrate
```

5. **Create a superuser:**
```bash
python manage.py createsuperuser
```

5. **Run the development server:**
```bash
python manage.py runserver
```

## Usage
- Navigate **to http://127.0.0.1:8000** in your web browser.
- Sign up for an account and log in.
- Start creating new topics and making entries.
