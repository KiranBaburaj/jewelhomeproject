"""
Django settings for jewel project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!1)rul!i0*5h$^q(^)5ab$8ctsfxp-v938pom&bb&cdqzn315*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
SOCIALACCOUNT_ADAPTER = 'allauth.socialaccount.adapter.DefaultSocialAccountAdapter'




# Application definition
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '408030459908-14mo58097h4qr7uen5s0n9ths4jls5en.apps.googleusercontent.com',
            'secret': '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',
        }
    },
    # Add other providers if used (e.g., 'facebook', 'twitter')
}

# settings.py
ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/profile/'

# settings.py

RAZORPAY_API_KEY = 'rzp_test_HHlRhM2dDivhld'
RAZORPAY_API_SECRET = '7ns64MRvik8KWRPU6SKUXT4A'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles','product','cadmin','rest_framework','user',  'wishlist','coupon',  'allauth',
    'allauth.account','allauth.socialaccount','allauth.socialaccount.providers.google','payments','corsheaders',
]

# settings.py
# Add the Twilio credentials


TWILIO_ACCOUNT_SID = 'ACe8cae81e087c6c60d31751fd56d7fd99'
TWILIO_AUTH_TOKEN = 'eb8a7fd3b2c48e57610370218ab62b84'

AUTHENTICATION_BACKENDS = [
    # ...
    'allauth.account.auth_backends.AuthenticationBackend', 
    # ...
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'jewel.urls'

# settings.py

CORS_ALLOW_ALL_ORIGINS = False



# settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",  # Add your frontend origin here
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'jewel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jewels',
        'USER': 'postgres',
        'PASSWORD': '916916',
        'HOST': 'localhost',  # Set to your PostgreSQL server host
        'PORT': '5432',       # Set to your PostgreSQL server port
    }
}

AUTH_USER_MODEL = 'user.User'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'uwantshim@gmail.com'
EMAIL_HOST_PASSWORD = 'srbn gmju dkkh ljgj'


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = BASE_DIR / 'staticfiles'