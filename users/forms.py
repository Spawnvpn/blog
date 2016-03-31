import datetime

import pickle
from django import forms
from django.contrib.auth import authenticate

from users.models import BlogUser


# class MultiWidgetBasic(forms.widgets.MultiWidget):
#     def __init__(self, attrs=None):
#         widgets = [forms.NumberInput(),
#                    forms.NumberInput(),
#                    forms.NumberInput()]
#         super(MultiWidgetBasic, self).__init__(widgets, attrs)
#
#     def decompress(self, value):
#         if value:
#             return pickle.loads(value)
#         else:
#             return ['', '']
#
#     def format_output(self, rendered_widgets):
#         return ('<div class="date-range form-inline">+' + rendered_widgets[0] +
#                 '(' + rendered_widgets[1] + ')' + rendered_widgets[2] +
#                 '</div>')
#
#
# class PhoneNumberField(forms.MultiValueField):
#     widget = MultiWidgetBasic
#
#     def __init__(self, *args, **kwargs):
#         fields = (forms.IntegerField(min_value=0),
#                   forms.IntegerField(min_value=0),
#                   forms.IntegerField(min_value=0),)
#         super(PhoneNumberField, self).__init__(fields=fields, *args, **kwargs)
#
#     def compress(self, data_list):
#         pass


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'fill-container'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'fill-container'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError(message='Invalid username or password',
                                        code='invalid_login')


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    birth_date = forms.DateField()
    # phone_number = PhoneNumberField()
    phone_number = forms.CharField()

    def clean_birth_date(self):
        date = self.cleaned_data.get("birth_date")
        today = datetime.date.today()
        if date.year >= today.year - 12:
            raise forms.ValidationError("You must grow up! SUKA")
        return date

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    class Meta:
        model = BlogUser
        fields = (
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name",
            "birth_date",
            "phone_number",
        )
