from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import customUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = customUser

    def get_readonly_fields(self, request, obj=None):
        if obj:
          if obj.is_active:
            return self.readonly_fields + ('employee_id',)
        return self.readonly_fields
        
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name', 'employee_id']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name','employee_id')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('employee_id',)}),
    )

admin.site.register(customUser, CustomUserAdmin)