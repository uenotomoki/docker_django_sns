import os

SECRET_KEY = 'django-insecure-%5074g=0r$x8p!rx=0iw(w@(2sbxx3vojt!-51!lllo7%usv(v'

#settings.pyからそのままコピー
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

#DEBUG = True