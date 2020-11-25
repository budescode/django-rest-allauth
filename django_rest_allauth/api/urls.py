from django.urls import path
from .views import SocialUserAuth, RegisterUserView, LoginUserView, UserDetails, ChangePasswordView, ResetPasswordCodeView, ResetPasswordView, userLogout, EditUserView
urlpatterns = [
    path('authenticatesocialuser', SocialUserAuth.as_view(), name='authenticatesocialuser'),
    path('token/createuser', RegisterUserView.as_view(), name='createuser'),
    path('token/login', LoginUserView.as_view(), name='login'),
    path('token/getuser', UserDetails.as_view(), name='getuser'),
    path('token/edituser', EditUserView.as_view(), name='edituser'),
    path('token/changepassword', ChangePasswordView.as_view(), name='changepassword'),
    path('token/resetpasswordcode', ResetPasswordCodeView.as_view(), name='resetpasswordcode'),
    path('token/resetpassword', ResetPasswordView.as_view(), name='resetpassword'),
    path('token/logout', userLogout, name='logout'),
]
