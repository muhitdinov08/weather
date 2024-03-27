from django.contrib.auth.models import User
from django.forms import ModelForm, ImageField, Form, CharField, PasswordInput

from weather.models import Weather


class UserRegisterForm(ModelForm):
    password = CharField(max_length=128, widget=PasswordInput)

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "email")


class UserLoginForm(Form):
    username = CharField(max_length=128)
    password = CharField(max_length=128, widget=PasswordInput)


class AddWeatherForm(ModelForm):
    city_name = CharField(max_length=128)

    class Meta:
        model = Weather
        fields = ["city_name"]


class SeeWeatherForm(ModelForm):
    city_name = CharField(max_length=128)

    class Meta:
        model = Weather
        fields = ['city_name']


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
