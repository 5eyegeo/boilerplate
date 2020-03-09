from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'username')


class TermsAgreeForm(forms.Form):
    tos = forms.BooleanField(required=True)

    def signup(self, request, user):
        user.tos = self.cleaned_data['tos']
        user.save()
        return user
