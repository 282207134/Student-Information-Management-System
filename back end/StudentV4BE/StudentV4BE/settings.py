"""
Django StudentV4BE プロジェクトの設定。
Django 3.0.14 の 'django-admin startproject' を使用して生成されました。
このファイルの詳細については、以下を参照してください：
https://docs.djangoproject.com/en/3.0/topics/settings/
すべての設定とその値の完全なリストについては、以下を参照してください：
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os, sys
from pathlib import Path
# プロジェクト内のパスを構築します。例：BASE_DIR / "subdir"。
BASE_DIR = Path(__file__).resolve().parent.parent
# ルートディレクトリに加えて、指定したディレクトリでもプログラムが実行されるようにします
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# 開発のためのクイック設定 - 本番では使用しないでください
# 詳細は https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/ を参照してください
# セキュリティ警告：本番環境で使用する秘密鍵を使用してください！
SECRET_KEY = 'e_$7=pplr33wg_)4q6+9)qu7v@0@1@sh09z4oxm#3+k40e4p6k'
# セキュリティ警告：デバッグを有効にしないでください！
DEBUG = True
ALLOWED_HOSTS = ['192.168.138.128']  # 他のコンピュータから接続する場合は、現在のバックエンドのIPアドレスを入力する必要があります
# python manage.py runserver 192.168.138.128:8000
# アプリケーションの定義
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student',
    'corsheaders',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'StudentV4BE.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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
WSGI_APPLICATION = 'StudentV4BE.wsgi.application'
# データベース
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'StudentV4DB',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
# パスワード検証
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validator
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# 静的ファイル（CSS、JavaScript、画像）
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
# アップロードファイルのディレクトリと外部アクセスパスを設定する
MEDIA_ROOT=os.path.join(BASE_DIR,'media/')
MEDIA_URL='/media/'
# ホワイトリストに含まれるドメインは、すべてバックエンドAPIにアクセスできます
CORS_ALLOW_CREDENTIALS = True  # CORSアクセス中に、バックエンドがクッキーを操作できるかどうかを指定します。
CORS_ALLOWED_ORIGINS = [  # フロントエンドIP
    "http://192.168.56.1:5500",
    # ここにVue.jsアプリケーションのアドレスを設定します
]
