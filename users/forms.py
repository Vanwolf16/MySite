from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput({'class':'focus:outline-none','placeholder':'demo@gmail.com'}))
    username = forms.CharField(required=True,widget=forms.TextInput({'class':'focus:outline-none','placeholder':'wolfie'}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput({'class':'focus:outline-none','placeholder':'password'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput({'class':'focus:outline-none','placeholder':'confirm password'}))

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user    
