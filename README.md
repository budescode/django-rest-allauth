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

* [token/createuser](#createuser)
* [token/login](#login)
* [token/getuser](#getuser)
* [token/edituser](#edituser)
* [token/changepassword](#changepassword)
* [token/resetpasswordcode](#resetpasswordcode)
* [token/resetpassword](#resetpassword)
* [token/logout](#logout)
* [authenticatesocialuser](#authenticatesocialuser)

### createuser 
- This is to create a user
- Method: POST
- Authorization: AllowAny
- fields:
{
"email": "",
"username": "",
"password": "",
"first_name": "",
"last_name": ""
}
- Optional fields are username, first_name and last_name



### login 
- This is to login a user, it returns userdetails with token along 
- Method: POST
- Authorization: AllowAny
- fields:
{
    "email": "",
    "username": "",
    "password": "",
}
- Optional either username or email can be used, or both.
It returns response with token along with it for authentication



### edituser 
- This is to edituser details
- Method: POST
- Authorization: Token
- fields:
{
    "email": "",
    "username": "",
    "first_name": "",
    "last_name": "",
}
- All fields are optional, only input the field you want to change

### changepassword 
- This is to change user's password
- Method: POST
- Authorization: Token
- fields:
{
    "old_password": "",
    "new_password": "",
}
- If the old password is correct, it changes the user's password to the new one.

### getuser 
- This is to get user details, it returns an object with the user details
- Method: GET
- Authorization: Token

### resetpasswordcode
- This will generate a code for the user and send back as response,  the code can be sent to the user's email or sms, the next end point will be to accept the code and email
- Method: POST
- Authorization: AllowAny
- fields: 
{
"email": "",
"resetcode": ""
}

### resetpassword
- This will accept the code, email and password, if it's correct, the password will be changed
- Method: POST
- Authorization: AllowAny
- fields: 
{
"email": "",
"resetcode": "",
"password": ""
}

### logout
- This will delete the user's token
- Method: POST
- Authorization: AllowAny


### authenticatesocialuser

- To authenticate a user with social media (facebook and google)
- Method: POST
- Authorization: AllowAny
- fields:
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
- These fields are coming from google/facebook response.
- ## provider field accepts 'Facebook' or 'Google'
- optional fields are username, first_name, last_name and profile_pic



