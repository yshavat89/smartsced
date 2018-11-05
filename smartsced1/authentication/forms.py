from .models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password']
    
class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password','email','group','image','first_name','last_name']  
