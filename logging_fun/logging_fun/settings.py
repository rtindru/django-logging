"""
Django settings for logging_fun project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Indrajit', 'rt.indru@gmail.com'),
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2%n&#zuxrddorwj##z(^xr1-abx4+r2--(vnfcxgh7g203ww=='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Host for sending e-mail.
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rt.indru@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'logging_fun',
    'unconfigured',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'logging_fun.urls'

WSGI_APPLICATION = 'logging_fun.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'logging_fun',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

DJANGO_LOG_LEVEL = DEBUG

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            # 'formatter': 'simple',
        },
        'root_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/root_file_handler.log',
            # 'formatter': 'verbose',
        },
        'django_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/django_file_handler.log',
            # 'formatter': 'verbose',
        },
        'app_file': {
            'level': 'DEBUG',
            # 'level': 'INFO',  # Step 2 - Handler Split
            'class': 'logging.FileHandler',
            'filename': '/tmp/app_file_handler.log',
            # 'formatter': 'verbose',
            'filters': ['filter_passwords'],
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/debug.log',
            # 'formatter': 'simple',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/tmp/exception.log',
            # 'formatter': 'verbose',
            # 'filters': ['filter_passwords'],
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            # 'filters': ['require_debug_false'],
            'include_html': True,
        }
    },
    'root': {  # Step 5 - Catch All
        'handlers': ['root_file', 'error_file', ],  #'mail_admins'],  # Step 7 - Errors
        'level': 'DEBUG',
    },
    'loggers': {
        'logging_fun': {
            'handlers': ['app_file', 'console', 'error_file'],  # Step 2 - Handler Splits
            'level': 'DEBUG',  # Step 1 - Normal Logging
            # 'level': 'INFO',  # Step 3 - Info Level Skips
            'propagate': True,
        },
        'logging_fun.buggy_module': {  # Step 4 - App level splits
            'handlers': ['debug_file'],
            'level': 'DEBUG',
            'propagate': True,  # Step 6 - Propagation
        },
        'django.request': {  # Step 8 - Django Request/Template/DB
            'handlers': ['django_file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['django_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    # 'formatters': {  # Step 9 - Formatters
    #     'verbose': {
    #         'format': '%(levelname)s %(asctime)s %(process)d %(thread)d %(module)s %(lineno)d :: %(message)s'
    #     },
    #     'simple': {
    #         'format': '%(levelname)s :: %(message)s'
    #     },
    # },
    'filters': {  # Step 10  - Filters
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'filter_passwords': {
            '()': 'logging_fun.buggy_module.PasswordObfuscationFilter'
        },
    },
}
