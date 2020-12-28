from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class customUser(AbstractUser):
    employee_id = models.CharField(verbose_name=_('Employee ID'),max_length=50, blank=True, null=True, validators=[alphanumeric], unique = True)
    #make this field readonly when user is active