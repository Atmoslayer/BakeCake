
INSTALLED_APPS = [
    'cakes.apps.CakesConfig',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC+3'

USE_I18N = True

USE_TZ = True
