from django import forms
from django.forms.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # Not needed here but is a nice snippet I'll be using later.
    # date_of_birth = forms.DateField(
    #     label="Date of Birth",    
    #     widget=SelectDateWidget(
    #         empty_label=("Choose Year", "Choose Month", "Choose Day"),
    #     ),
    # )
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
