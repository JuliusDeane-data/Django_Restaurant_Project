from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    show = forms.BooleanField(label="Show Password",
                              widget=forms.CheckboxInput(
                                  attrs={
                                      'class': 'show-password',
                                  }
                              ),
                              required=False)