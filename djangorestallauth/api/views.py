from djangorestallauth.models import DjangoRestAllAuth
from .serializers import SocialSerializer, UserSerializer, UserLoginSerializer, UserDetailsSerializer, ChangePasswordSerializer, ResetPasswordSerializer
from rest_framework import generics
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
import random
import string
from random import choice
User = get_user_model()


class UserDetails(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = UserDetailsSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get_object(self):
        user = User.objects.get(username=self.request.user.username)
        return user


class ChangePasswordView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ChangePasswordSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid(): 
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            user = self.request.user
            check = user.check_password(old_password)
            if check:                
                user.set_password(new_password)
                user.save()
                data = {'message':'Password Successfully Changed'}
                return Response(data, status=HTTP_200_OK)
            else:
                data = {"message":"Invalid Password"}
                return Response(data, status=HTTP_400_BAD_REQUEST)
        else:
            data = {"message":serializer.errors}
            return Response(data, status=HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        qs = []
        return qs

class LoginUserView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserLoginSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(): 
            password = serializer.validated_data['password']
            if 'email' in serializer.validated_data and 'username' in serializer.validated_data: #if the email and username is passed, authenticate with both
                email = serializer.validated_data['email']
                username = serializer.validated_data['username']
                print(username, email, password, 'yayyaay')
                user = authenticate(username=username, password=password)
                print(user)
                if user is not None:
                    if user.is_active:
                        user_token = Token.objects.get_or_create(user=user)
                        user_token = user_token[0]
                        user_token = user_token.key
                        userdetails = {}
                        userdetails['username'] = user.username
                        userdetails['email'] = user.email
                        userdetails['token'] = user_token
                        userdetails['first_name'] = user.first_name
                        userdetails['last_name'] = user.last_name
                        return Response(userdetails, status=HTTP_200_OK)
                else:
                    data = {"message":"Invalid Login Details"}
                    return Response(data, status=HTTP_400_BAD_REQUEST)
                
            elif 'email' in serializer.validated_data: #if email is passed, authenticate with email
                email = serializer.validated_data['email']
                theu = email.find('@')
                username = email[:theu]
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        user_token = Token.objects.get_or_create(user=user)
                        user_token = user_token[0]
                        user_token = user_token.key
                        userdetails = {}
                        userdetails['username'] = user.username
                        userdetails['email'] = user.email
                        userdetails['token'] = user_token
                        userdetails['first_name'] = user.first_name
                        userdetails['last_name'] = user.last_name
                        return Response(userdetails, status=HTTP_200_OK)
                else:
                    data = {"message":"Invalid Login Details"}
                    return Response(data, status=HTTP_400_BAD_REQUEST)
            elif 'username' in serializer.validated_data: #if username is passed, authenticate with username
                username = serializer.validated_data['username']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        user_token = Token.objects.get_or_create(user=user)
                        user_token = user_token[0]
                        user_token = user_token.key
                        userdetails = {}
                        userdetails['username'] = user.username
                        userdetails['email'] = user.email
                        userdetails['token'] = user_token
                        userdetails['first_name'] = user.first_name
                        userdetails['last_name'] = user.last_name
                        return Response(userdetails, status=HTTP_200_OK)
                else:
                    data = {"message":"Invalid Login Details"}
                    return Response(data, status=HTTP_400_BAD_REQUEST)
        else:
            data = {"message":serializer.errors}
            return Response(data, status=HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        qs = []
        return qs

class RegisterUserView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            last_name = ''
            first_name = ''
            password = serializer.validated_data['password']
            if 'last_name' in serializer.validated_data:
                last_name = serializer.validated_data['last_name']            
            if 'first_name' in serializer.validated_data:
                first_name = serializer.validated_data['first_name']
            if 'email' in serializer.validated_data and 'username' in serializer.validated_data:                
                email = serializer.validated_data['email']
                username = serializer.validated_data['username']
                print(email, username, password, 'registr')
                user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                message = {'username':username, 'email':email, 'first_name':first_name, 'last_name':last_name}
                return Response(message, status=HTTP_201_CREATED)
            elif 'email' in serializer.validated_data:
                email = serializer.validated_data['email']
                theu = email.find('@')
                username = email[:theu]
                user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                message = {'username':username, 'email':email, 'first_name':first_name, 'last_name':last_name}
                return Response(message, status=HTTP_201_CREATED)
        else:
            data = {"message":serializer.errors}
            return Response(data, status=HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        qs = []
        return qs


class SocialUserAuth(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = SocialSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    def post(self, request, format=None):
        serializer = SocialSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            authmode = serializer.validated_data['authmode']
            token = serializer.validated_data['token'] 
            social_id = serializer.validated_data['social_id'] 
            try:
                serializer.validated_data['username']
                username = serializer.validated_data['username']
                try:
                    user = User.objects.get(username=username)
                    if user is not None:
                        if user.is_active:
                            user_token = Token.objects.get_or_create(user=user)
                            user_token = user_token[0]
                            user_token = user_token.key
                            user.token = user_token
                            user.save()
                            DjangoRestAllAuth.objects.get_or_create(user=user, authmode=authmode, token=token, email=email, username=username, social_id=social_id)
                            userdetails = {}
                            userdetails['username'] = user.username
                            userdetails['email'] = user.email
                            userdetails['token'] = user_token
                            return Response(userdetails, status=HTTP_201_CREATED)
                except:
                    allchar = string.ascii_letters + string.digits
                    password = ''.join(choice(allchar) for x in range(13))
                    user = User.objects.create(username=username, email=email, password=password)
                    user_token = Token.objects.get_or_create(user=user)
                    user_token = user_token[0]
                    user_token = user_token.key
                    user.token = user_token
                    user.save()
                    DjangoRestAllAuth.objects.get_or_create(user=user, authmode=authmode, token=token, email=email, username=username, social_id=social_id)
                    userdetails = {}
                    userdetails['username'] = user.username
                    userdetails['email'] = user.email
                    userdetails['token'] = user_token
                    return Response(userdetails, status=HTTP_201_CREATED)
            except KeyError:
                email = serializer.validated_data['email']
                theu = email.find('@')
                username = email[:theu]
                try:
                    user = User.objects.get(username=username)
                    if user is not None:
                        if user.is_active:
                            user_token = Token.objects.get_or_create(user=user)
                            user_token = user_token[0]
                            user_token = user_token.key
                            user.token = user_token
                            user.save()
                            DjangoRestAllAuth.objects.get_or_create(user=user, authmode=authmode, token=token, email=email, username=username, social_id=social_id)
                            userdetails = {}
                            userdetails['username'] = user.username
                            userdetails['email'] = user.email
                            userdetails['token'] = user_token
                            return Response(userdetails, status=HTTP_201_CREATED)
                except:
                    allchar = string.ascii_letters + string.digits
                    password = ''.join(choice(allchar) for x in range(13))
                    user = User.objects.create(username=username, email=email, password=password)
                    user_token = Token.objects.get_or_create(user=user)
                    user_token = user_token[0]
                    user_token = user_token.key
                    user.token = user_token
                    user.save()
                    DjangoRestAllAuth.objects.get_or_create(user=user, authmode=authmode, token=token, email=email, username=username, social_id=social_id)
                    userdetails = {}
                    userdetails['username'] = user.username
                    userdetails['email'] = user.email
                    userdetails['token'] = user_token
                    return Response(userdetails, status=HTTP_201_CREATED)
            else:
                data = {"message":"not found", "results":[]}
                return Response(data, status=HTTP_400_BAD_REQUEST)
        else:
            data = {"message":serializer.errors, "results":[]}
            return Response(data, status=HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        qs = []
        return qs


def create_token(user):
    user_token = Token.objects.get_or_create(user=user)
    user_token = user_token[0]
    user_token = user_token.key
    user.token = user_token
    user.save()
    return user_token
  