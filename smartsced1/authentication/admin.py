from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import User


class MyUserAdmin(UserAdmin):

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','group', 'password1', 'password2', ),
        }),
        (None , {
            'classes': ('wide',),
            'fields': ('department', ),
        }),
        ('Personal Details', {
            'classes': ('wide',),
            'fields':('first_name', 'last_name','phone','email')
        }),
    )

    list_display = ('username','group','first_name', 'email')
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('group','department','phone',)}),
    )
    

admin.site.register(User, MyUserAdmin)
