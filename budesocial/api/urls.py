from django.urls import path
from .views import BudeSocialView, UserCreateView, SocialUserAuth
urlpatterns = [
    path('budesocial/<slug:pk>', BudeSocialView.as_view(), name='budesocialurl'),
    path('createuser', SocialUserAuth.as_view(), name='createuser'),
    #path('createuser', UserCreateView.as_view(), name='createuser'),
]
