from .settings import *

# Use SQLite for quick local runs to avoid needing Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Allow all hosts for local testing
ALLOWED_HOSTS = ['*']
