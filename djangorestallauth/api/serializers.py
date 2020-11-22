from rest_framework import serializers
from djangorestallauth.models import DjangoRestAllAuth
from django.conf import settings
from rest_framework.authtoken.models import Token
import requests
from django.contrib.auth import get_user_model
User = get_user_model()

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField()
    def validate(self, data):
        email = data['email']
        if not 'email' in data and not 'username' in data :
            raise serializers.ValidationError('Enter Username Or Email')        
        return data

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()



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


def sendRequest(url):
    try:
        r = requests.get(url = url)         
        data = r.json() 
    except ConnectionError:
        data = {'network':'unable to connect, check your data connection'}
    return data


class SocialSerializer(serializers.ModelSerializer):
    #password = serializers.CharField(write_only = True, required=True)
    class Meta:
        model = DjangoRestAllAuth
        fields = '__all__'
        read_only_fields = ['user', 'pk']

    def validate(self, data):
        authmode = data['authmode']
        token = data['token']
        fburl = 'https://graph.facebook.com/me?access_token={}'.format(token)
        googleurl = 'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={}'.format(token)
        githuburl = 'https://api.github.com/applications/:client_id/tokens/:token={}'.format(token)
        if authmode == 'Facebook':
            fbrequest = sendRequest(fburl)
            print(fbrequest)
            if not 'id' in fbrequest:
                raise serializers.ValidationError('Invalid token or has expired')   
        if authmode == 'Google':
            googlerequest = sendRequest(googleurl)
            print(googlerequest)
            if not 'user_id' in googlerequest:
                raise serializers.ValidationError('Invalid token or has expired')   
        return data
    
    # def validate_token(self, value):
    #     url = 'https://graph.facebook.com/me?access_token={}'.format(value)
    #     try:
    #         r = requests.get(url = url)         
    #         data = r.json() 
    #         print(data, 'yayayaya')
    #         try:
    #             userid = data['id']
    #         except KeyError:
    #             raise serializers.ValidationError('Invalid token or has expired')
    #     except ConnectionError:
    #         raise serializers.ValidationError('Unable to validate token, make sure your data connection is on')
    #     return value
