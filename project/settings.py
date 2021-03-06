import os

from environs import Env

env = Env()
env.read_env()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": env.str("DB_HOST"),
        "PORT": env.int("DB_PORT"),
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASSWORD"),
    }
}

SECRET_KEY = os.environ["DB_SECRET_KEY"]

INSTALLED_APPS = ["datacenter"]

DEBUG = env.bool("DEBUG", default=False)

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ["*"]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
    }
]

USE_TZ = True

TIME_ZONE = "Europe/Moscow"

USE_L10N = True

LANGUAGE_CODE = "ru-ru"
