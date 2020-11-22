from django.db import models
from django.conf import settings

class BudeSocialModel(models.Model):
    social_choice = (
        ('Facebook', 'Facebook'),
        ('Google', 'Google'),
        ('Twitter', 'Twitter'),
        ('Github', 'Github'),
    )
    authmode = models.CharField(max_length=20, choices=social_choice)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.TextField()
    email = models.EmailField()
    username = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    social_id = models.TextField()
    profile_pic  =  models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username