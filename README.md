# django-rest-allauth
A Django app to handle rest framework authentications

Quick start
-----------
1. Install Dep:
    pip install django-rest-framework django-cors-headers requests

2. Add "django_rest_allauth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_rest_allauth',
        'rest_framework',
        'rest_framework.authtoken',
        'corsheaders',
    ]

3. Include corsheaders in your middleware in settings.py
    MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
    ]

4. Include the django_rest_allauth URLconf in your project urls.py like this::

    path('django-rest-allauth/', include('django-rest-allauth.api.urls')),

5. Set how you want your corsheaders in settings.py or whitelist your url
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_ALLOW_ALL = True
    SITE_ID = 1

6. Run ``python manage.py makemigrations`` ``python manage.py migrate`` to create the DjangoRestAllAuth models.

7. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

8. Visit http://127.0.0.1:8000/django-rest-allauth/ to participate in the django_rest_allauth.

## Url Endpoints
This package uses token authentication
* [authenticatesocialuser](#authenticatesocialuser)
* [token/createuser](#createuser)
* [token/login](#login)
* token/getuser
* token/edituser
* token/changepassword
* token/resetpasswordcode
* token/resetpassword
* token/logout


### createuser 
This is to create a user
fields:
{
    "email": "",
    "username": "",
    "password": "",
    "first_name": "",
    "last_name": ""
}
Optional fields are username, first_name and last_name



### login 
This is to create a user
fields:
{
    "email": "",
    "username": "",
    "password": "",
}
Optional either username or email can be used, or both.
It returns response with token along with it for authentication


### authenticatesocialuser

To authenticate a user with social media (facebook and google)
fields:
{
    "provider": '',
    "token": "",
    "email": "",
    "username": "",
    "first_name": "",
    "last_name": "",
    "social_id": "",
    "profile_pic": ""
}
These fields are coming from google/facebook response.
provider accepts 'Facebook' or 'Google'
optional fields are username, first_name, last_name and profile_pic



