# Django CAPTCHA Project

A Django web application demonstrating CAPTCHA integration for form validation using django-simple-captcha.


## Installation

1. Clone the repository or download the project files

2. Install required packages:

```bash
pip install django
pip install django-simple-captcha
pip install Pillow
```

3. Apply database migrations:

```bash
python manage.py migrate
```

4. Create a superuser (optional, for admin access):

```bash
python manage.py createsuperuser
```

## Running the Application

1. Start the development server:

```bash
python manage.py runserver
```

2. Open your web browser and navigate to:

```
http://127.0.0.1:8000/
```

3. You should see the login form with CAPTCHA verification

## Project Structure

```
django-captcha/
├── accounts/              # Accounts application
│   ├── forms.py          # Login form with CAPTCHA field
│   ├── views.py          # View logic for login
│   ├── urls.py           # URL routing for accounts
│   └── templates/        # HTML templates
│       └── accounts/
│           └── login.html
├── my_site/              # Main project configuration
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── db.sqlite3            # SQLite database
└── manage.py             # Django management script
```

## Configuration

### CAPTCHA Settings

The CAPTCHA is configured in the `INSTALLED_APPS` section of `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'captcha',
    'accounts',
]
```

### URL Configuration

CAPTCHA URLs are included in the main `urls.py`:

```python
urlpatterns = [
    path('captcha/', include('captcha.urls')),
    ...
]
```

## Usage

1. Navigate to the login page
2. Enter a username and password
3. Solve the CAPTCHA challenge
4. Submit the form
5. You will receive feedback on whether the CAPTCHA was validated correctly

## Customization

### Modifying CAPTCHA Appearance

You can customize the CAPTCHA appearance by adding settings to `settings.py`:

```python
CAPTCHA_IMAGE_SIZE = (150, 50)
CAPTCHA_FONT_SIZE = 30
CAPTCHA_LETTER_ROTATION = (-35, 35)
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_FOREGROUND_COLOR = '#001100'
```

### Adjusting CAPTCHA Difficulty

```python
CAPTCHA_LENGTH = 6  # Number of characters
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'  # Use math challenges
```

## Security Notes

- The `SECRET_KEY` in settings.py should be kept secret in production
- Set `DEBUG = False` in production environments
- Configure `ALLOWED_HOSTS` for production deployment
- Use environment variables for sensitive configuration

## Troubleshooting

### CAPTCHA images not showing

- Ensure Pillow is installed: `pip install Pillow`
- Run migrations: `python manage.py migrate`

### Database errors

- Delete `db.sqlite3` and run migrations again:

```bash
rm db.sqlite3
python manage.py migrate
```

## Development

This project uses Django 6.0 and follows standard Django project structure. The CAPTCHA functionality is isolated in the accounts app, making it easy to integrate into other Django projects.

## License

This project is created for learning purposes.

## Contributing

This is a learning project. Feel free to fork and modify for your own educational purposes.
