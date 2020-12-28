from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.signals import user_logged_in

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class customUser(AbstractUser):
    employee_id = models.CharField(verbose_name=_('Employee ID'),max_length=50, blank=True, null=True, validators=[alphanumeric], unique = True)
    login_cnt = models.IntegerField(verbose_name=_('Login count'), default=0, blank=True, null=True)

def update_user_login(sender, user, **kwargs):
    user.login_cnt = user.login_cnt + 1
    user.save()

user_logged_in.connect(update_user_login)