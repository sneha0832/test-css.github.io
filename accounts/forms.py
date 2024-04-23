from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from csctest.models import ExhibitRating
from .models import UserProfile
from .models import Child


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'birthdate', 'gender']
