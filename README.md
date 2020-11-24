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

### authenticatesocialuser

Hello, this is some text to fill in this, [here](#authenticatesocialuser), is a link to the sauthenticatesocialuser.

### authenticatesocialuser

Place one has the fun times of linking here, but I can also link back [here](#place-1).

### Place's 3: other example

Place one has the fun times of linking here, but I can also link back [here](#places-3-other-example).
