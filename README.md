# Crelio-UserListing-backend
Backend code for User listing app

Crelio app consists of backend and a frontend

backend code - https://github.com/pankaj-j-sharma/Crelio-UserListing-backend.git
frontend code - https://github.com/pankaj-j-sharma/Crelio-UserListing-frontend.git

we need to install the python libraries as mentioned in requirements.txt

Python 3.8.0 is used in this app 
Database used is sqlite which is the default one for django 
ORM system of the django has been utilised so we can use any other database also 
for that we need to modify the below configuration in setting.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


cd backend
python -m pip install -r requirements.txt
python manage.py runserver
sample user is admin with cred 12345



