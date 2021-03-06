"""
Django settings for proyectoferreteria project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd=(hv!wxw*67r3w*9=bo6lws9p6v+sf_02k=+*hj&*szj5@daz'

# SECURITY WARNING: don't run with debug turned on in production!
DJANGO_ADMIN_LOGS_DELETABLE  =  True
DEBUG = True

ALLOWED_HOSTS = []
LOGIN_HOST = 'Vista_principal'
LOGIN_REDIRECT_URL = 'Vista_principal'

# Application definition

INSTALLED_APPS = [
    'vali',
    
    'django.contrib.admin',
    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'proyectoferreteria.apps.gestionadmin',
    'django_admin_logs', 
    'django_db_logger',
    'logs',
    'blacklist',
    'axes',
    'data_browser',
    'reports',
    
    
      
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'blacklist.middleware.blacklist_middleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'axes.middleware.AxesMiddleware',
      
]

ROOT_URLCONF = 'proyectoferreteria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[os.path.join(BASE_DIR, 'templates')],
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

EXCEL_SUPPORT = 'xlwt' # or 'openpyxl' or 'pyexcelerator
DATA_BROWSER_ALLOW_PUBLIC: False
DATA_BROWSER_AUTH_USER_COMPAT: True
DATA_BROWSER_DEFAULT_ROW_LIMIT: 1000
DATA_BROWSER_DEV: False
DATA_BROWSER_FE_DSN = "https://af64f22b81994a0e93b82a32add8cb2b@o390136.ingest.sentry.io/5231151"


VALI_CONFIG = {
        'theme': 'green',
        'dashboard': {
            'name': 'KONTROOL',
            'url': '/admin/dashboard/',
            'subtitle': 'KONTROOL',
            'site_name': 'KONTROOL',
            'url_image_profile': 'https://i.ibb.co/KjBytn3/KONTROOL-LOGO.png'
        },
        'fieldset': {
            'fields': ['user_permissions', 'permissions']
        },
        'applist': {
            'order': "registry", "group": True
        }
    }  


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}

MIDDLEWARE_CLASSES = (
'django.middleware.common.CommonMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'axes.middleware.FailedLoginMiddleware'

)

AXES_LOGIN_FAILURE_LIMIT: ['axes.W003']
AXES_LOCK_OUT_AT_FAILURE: True
AXES_USE_USER_AGENT: True

SILENCED_SYSTEM_CHECKS = ['axes.W003']
AXES_ENABLED = True
AXES_ONLY_USER_FAILURES = True



AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]


WSGI_APPLICATION = 'proyectoferreteria.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

import datetime
now=datetime.datetime.now()

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-spanish'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


