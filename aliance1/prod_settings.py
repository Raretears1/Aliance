import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-yfl1$ax779wo*dsg462wfsw((&3%3)vgbp12mv+t*j!w+w8+wg2v7'

DEBUG = False

ALLOWED_HOSTS = ["aliance-irpen.com.ua", "wwww.aliance-irpen.com.ua"]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
