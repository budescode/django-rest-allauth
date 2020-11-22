from budesocial.models import BudeSocialModel
from .serializers import BudeSocialSerializer
from rest_framework import generics
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import random
import string
from random import choice
User = get_user_model()

class SocialUserAuth(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BudeSocialSerializer
    # pagination_class = PostLimitOffsetPagination
    permission_classes = [
        permissions.AllowAny
    ]
    def post(self, request, format=None):
        serializer = BudeSocialSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            authmode = serializer.validated_data['authmode']
            token = serializer.validated_data['token'] 
            social_id = serializer.validated_data['social_id'] 
            try:
                serializer.validated_data['username']
                username = serializer.validated_data['username']
                print('1')
                try:
                    print('2')
                    user = User.objects.get(username=username)
                    if user is not None:
                        if user.is_active:
                            user_token = Token.objects.get_or_create(user=user)
                            user_token = user_token[0]
                            user_token = user_token.key
                            user.token = user_token
                            user.save()
                            BudeSocialModel.objects.get_or_create(user=user, authmode=authmode, token=token, email=email, username=username, social_id=social_id)
                            userdetails = {}
                            userdetails['username'] = user.username
                            userdetails['email'] = user.email
                            userdetails['token'] = user_token
                            return Response(userdetails, status=HTTP_201_CREATED)
                except:
                    print('3')
                    allchar = string.ascii_letters + string.digits
                    password = ''.join(choice(allchar) for x in range(13))
                    user = User.objects.create(username=username, email=email, password=password)
                    user_token = Token.objects.get_or_create(user=user)
                    user_token = user_token[0]
                    user_token = user_token.key
                    user.token = user_token
                    user.save()
                    BudeSocialModel.objects.get_or_create(user=user, authmode=authmode, token=token, email=email, username=username, social_id=social_id)
                    userdetails = {}
                    userdetails['username'] = user.username
                    userdetails['email'] = user.email
                    userdetails['token'] = user_token
                    return Response(userdetails, status=HTTP_201_CREATED)
            except KeyError:
                print('4')                
                email = serializer.validated_data['email']
                theu = email.find('@')
                username = email[:theu]
                try:
                    print('5')
                    user = User.objects.get(username=username)
                    if user is not None:
                        if user.is_active:
                            user_token = Token.objects.get_or_create(user=user)
                            user_token = user_token[0]
                            user_token = user_token.key
                            user.token = user_token
                            user.save()
                            BudeSocialModel.objects.get_or_create(user=user, authmode=authmode, token=token, email=email, username=username, social_id=social_id)
                            userdetails = {}
                            userdetails['username'] = user.username
                            userdetails['email'] = user.email
                            userdetails['token'] = user_token
                            return Response(userdetails, status=HTTP_201_CREATED)
                except:
                    print('6')
                    print('authenticating with email already exist')
                    allchar = string.ascii_letters + string.digits
                    password = ''.join(choice(allchar) for x in range(13))
                    user = User.objects.create(username=username, email=email, password=password)
                    user_token = Token.objects.get_or_create(user=user)
                    user_token = user_token[0]
                    user_token = user_token.key
                    user.token = user_token
                    user.save()
                    BudeSocialModel.objects.get_or_create(user=user, authmode=authmode, token=token, email=email, username=username, social_id=social_id)
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
class BudeSocialView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = BudeSocialSerializer

    def get_queryset(self):
        return BudeSocialModel.objects.all()

def create_token(user):
    user_token = Token.objects.get_or_create(user=user)
    user_token = user_token[0]
    user_token = user_token.key
    user.token = user_token
    user.save()
    return user_token
    
class UserCreateView(generics.CreateAPIView):
    serializer_class = BudeSocialSerializer
    def perform_create(self, serializer):
        email = serializer.validated_data['email']
        try:
            serializer.validated_data['username']
            username = serializer.validated_data['username']
            print('theres username')
            try:
                user = User.objects.get(username=username)
                if user is not None:
                    if user.is_active:
                        user_token = Token.objects.get_or_create(user=user)
                        user_token = user_token[0]
                        user_token = user_token.key
                        user.token = user_token
                        user.save()
            except:
                allchar = string.ascii_letters + string.digits
                password = ''.join(choice(allchar) for x in range(13))
                user = User.objects.create(username=username, email=email, password=password)
                user_token = Token.objects.get_or_create(user=user)
                user_token = user_token[0]
                user_token = user_token.key
                user.token = user_token
                user.save()
        except KeyError:
            print('nahhh')
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
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
            except:
                allchar = string.ascii_letters + string.digits
                password = ''.join(choice(allchar) for x in range(13))
                user = User.objects.create(username=username, email=email, password=password)
                user_token = Token.objects.get_or_create(user=user)
                user_token = user_token[0]
                user_token = user_token.key
                user.token = user_token
                user.save()

        # authmode = serializer.validated_data['authmode']
        # token = serializer.validated_data['token']
        # first_name = serializer.validated_data['first_name']
        # last_name = serializer.validated_data['last_name']
        # social_id = serializer.validated_data['social_id']
        # profile_pic = serializer.validated_data['profile_pic']                                                                
        # print(email, 'yeahhh')
        # user = get_user_model().objects.get(id=1)
        serializer.save(user=user)
    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'yeah': 'yeahh'
        }

    # def get_serializer_context(self, *args, **kwargs):
    #     serializer_class = self.get_serializer_class()
    #     kwargs["context"] = self.get_serializer_context()
    #     draft_request_data = self.request.data.copy()
    #     draft_request_data["first_name"] = 'name'
    #     draft_request_data["last_name"] = 'surname'
    #     draft_request_data["test"] = 'testt'
    #     kwargs["data"] = draft_request_data
    #     return serializer_class(*args, **kwargs)
    def get_serializer_context(self, **kwargs):
        context = {}
        # campaign = self.get_campaigns()[0]
        context['campaign_name'] = 'campaign.name'
        context['campaign_start_date'] = 'campaign.start_date'
        print('dxghxch')
        return context
    # def get_serializer_context(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     #context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     print('donee')
    #    # context['theos'] = 'yeahhhh'
    #     return {'context':'ya'}
