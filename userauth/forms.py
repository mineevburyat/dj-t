from django import forms
from django.contrib.auth import models



class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,
                               min_length=4,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100,
                               min_length=4,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # next = forms.URLField(required=False)
    
# class CreateUserForm(forms.ModelForm):
#     class Meta:
#         model = models.User
#         fields = ('username', 'lastname', 'firstname', 'password1', 'password2')