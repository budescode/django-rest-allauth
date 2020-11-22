from rest_framework import serializers
from budesocial.models import BudeSocialModel
from django.conf import settings
from rest_framework.authtoken.models import Token
import requests

def sendRequest(url):
    try:
        r = requests.get(url = url)         
        data = r.json() 
    except ConnectionError:
        data = {'network':'unable to connect, check your data connection'}
    return data


class BudeSocialSerializer(serializers.ModelSerializer):
    #password = serializers.CharField(write_only = True, required=True)
    class Meta:
        model = BudeSocialModel
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
