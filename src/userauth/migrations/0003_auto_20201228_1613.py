# Generated by Django 3.1.4 on 2020-12-28 16:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_customuser_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='login_cnt',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Login count'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='employee_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Employee ID'),
        ),
    ]
