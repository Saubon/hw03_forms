import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=t6&q$ovp$o!i5s9269o^0s0co&)@3+@dv4p3upy*o8sqtqe(2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'posts.apps.PostsConfig',  # Добавлено 23.02.2022
    'users.apps.UsersConfig',  # Добавлено 23.03.2022
    'core.apps.CoreConfig',  # Добавлено 23.03.2022
    'about.apps.AboutConfig',  # Добавлено 07.04.2022
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yatube.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')  # Добавлено 25.02.2022

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.year.year',  # Добавлено 05.04.2022
            ],
        },
    },
]

WSGI_APPLICATION = 'yatube.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = 'users:login'

LOGIN_REDIRECT_URL = 'posts:index'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')
