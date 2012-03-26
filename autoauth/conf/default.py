'default settings'
from datetime import timedelta

AUTOAUTH_EXPIRY = timedelta(days=1)

# here so tests work.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'autoauth.db'
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
]
