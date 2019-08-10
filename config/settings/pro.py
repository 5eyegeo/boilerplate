from .base import *  # noqa
from .base import env


DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env(
    "SECRET_KEY",
)

ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']


# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# DATABASES
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
    # read os.environ['SQLITE_URL']
    # 'extra': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db')
}
