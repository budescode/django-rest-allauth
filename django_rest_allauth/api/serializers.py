from rest_framework import serializers
from django_rest_allauth.models import DjangoRestAllAuth, ResetPasswordCode
from django.conf import settings
from rest_framework.authtoken.models import Token
import requests
from django.contrib.auth import get_user_model
User = get_user_model()

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    resetcode = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        email = data['email']
        resetcode = data['resetcode']
        qs = ResetPasswordCode.objects.filter(email=email, resetcode=resetcode)
        if not qs.exists():
            raise serializers.ValidationError('Invalid Email Or ResetCode')
        return data
    
class ResetPasswordCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResetPasswordCode
        exclude = []
    def validate(self, data):
        email = data['email']
        qs = User.objects.filter(email=email)
        if not qs.exists():
            raise serializers.ValidationError('Email Does Not Exist')
        return data

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField()
    def validate(self, data):
        email = data['email']
        if not 'email' in data and not 'username' in data :
            raise serializers.ValidationError('Enter Username Or Email')        
        return data

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    def validate(self, data):
        email = data['email']
        if not 'email' in data and not 'username' in data :
            raise serializers.ValidationError('Enter Username Or Email')        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email Already Exist')
        if 'username' in data:
            username = data['username']
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError('Username Already Exist')
        return data

class EditUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user.exists():
            raise serializers.ValidationError('email already exist')
        return value
    def validate_username(self, value):
        user = User.objects.filter(username=value)
        if user.exists():
            raise serializers.ValidationError('Username already exist')
        return value

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoRestAllAuth
        fields = '__all__'
        read_only_fields = ['user', 'pk', 'username']

    def sendRequest(self, url):
        try:
            r = requests.get(url = url)         
            data = r.json() 
        except ConnectionError:
            data = {'network':'unable to connect, check your data connection'}
        return data

    def validate(self, data):
        provider = data['provider']
        token = data['token']
        social_id = data['social_id']
        socialurl = {
            'fb':'https://graph.facebook.com/{}?fields=email&access_token={}'.format(social_id, token),
             'google': 'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={}'.format(token),
        }
        if provider == 'Facebook':
            fbrequest = self.sendRequest(socialurl['fb'])
            try:
                email = data['email']
                socialemail = fbrequest['email']
                if email != socialemail:
                    raise serializers.ValidationError('Input Right Email') 
                if social_id!= fbrequest['id']:
                    raise serializers.ValidationError('Invalid Social Id')
            except KeyError:
                raise serializers.ValidationError('Invalid token or has expired')                      
        if provider == 'Google':
            googlerequest = self.sendRequest(socialurl['google'])
            try:
                email = data['email']
                socialemail = googlerequest['email']
                if email != socialemail:
                    raise serializers.ValidationError('Input Right Email')
                if social_id!=googlerequest['user_id']:
                    raise serializers.ValidationError('Invalid Social Id')
            except KeyError:
                raise serializers.ValidationError('Invalid token or has expired') 
        return data
 