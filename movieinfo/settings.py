"""
Django settings for movieinfo project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta #JWT 로그인/로그아웃기능 설정
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d!cta0*f-pp7o43^jd4=3x+te7t0h)1=4nxhnp+t(2q*kd#wi%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


SIMPLE_JWT = {
    'USER_ID_FIELD': 'userid',  # 커스텀 필드 설정
    'USER_ID_CLAIM': 'user_id',
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ROTATE_REFRESH_TOKENS': False,    # 블랙리스트 설정
    'BLACKLIST_AFTER_ROTATION': True,  
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #추가
    'rest_framework',
    'accounts',        #기본 내 프로젝트
    'movieinfo',
    'kobis',
    'tmdb',
    'ai',
    'corsheaders', #프론트엔드 통신
    'rest_framework_simplejwt.token_blacklist',   #블랙리스트 기능
    'drf_yasg',  #스웨거 사용 
]



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ), #프레임워크 로그인/로그아웃기능

    # 페이지네이션을 위한 설정
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,  # 한 페이지당 12개의 항목
}                                                                     


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', #CORS추가
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #추가
    'corsheaders.middleware.CorsMiddleware', #프론트엔드 통신
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')      #프로필이미지 불러오기


#커스텀 모델 추가
AUTH_USER_MODEL = 'accounts.User'

CORS_ALLOW_ALL_ORIGINS = True  #임시적 !  모드 도메인 CORS 허용 (중요 )

ROOT_URLCONF = 'movieinfo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


SWAGGER_SETTINGS = {                           #스웨거 세팅 추가
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
}


swagger_path = "your/actual/path/to/swagger.json"


WSGI_APPLICATION = 'movieinfo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

# 정적 파일 디렉토리
STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",  # 'staticfiles' 디렉토리를 지정
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# 정적 파일 URL 경로
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_ROOT = BASE_DIR / "static"  # 배포 환경에서 collectstatic 명령어로 파일이 저장됨


# KOBIS API 설정
KOBIS_API_KEY = 'f0bbda432fe7324b506a3497b1503048'
KOBIS_API_BASE_URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest'

# TMDB API 설정
TMDB_BEARER_TOKEN = config('TMDB_BEARER_TOKEN')
TMDB_API_BASE_URL = 'https://api.themoviedb.org/3'
