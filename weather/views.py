from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
import requests
from django.views.generic import ListView

from weather.forms import UserLoginForm, UserRegisterForm, AddWeatherForm, SeeWeatherForm, UserUpdateForm
from weather.models import Weather


class HomePageView(View):
    def get(self, request):
        return render(request, 'weather/home.html')


class WeatherListView(ListView):
    def get(self, request, **kwargs):
        weather_list = Weather.objects.all()
        return render(request, 'weather/weather_list.html', {'weather_list': weather_list})


class AddWeather(View):
    def get(self, request):
        form = AddWeatherForm(data=request.GET)

        return render(request, 'weather/add_city_weather.html', context={'form': form})

    def post(self, request):
        form = AddWeatherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Weather successfully added')
            return redirect(reverse('weather:weather_list'))
        else:
            return render(request, 'weather/add_city_weather.html', context={'form': form})


class SeeWeather(View):
    def get(self, request):
        form = SeeWeatherForm(data=request.GET)
        return render(request, 'weather/see_weather.html', {'form': form})

    def post(self, request):
        form = SeeWeatherForm(data=request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            url = "https://weatherapi-com.p.rapidapi.com/current.json"

            querystring = {"q": f'{city_name}'}

            headers = {
                "X-RapidAPI-Key": "fa7da28988mshdfeb99f8717f94fp17da39jsn727e95c2c4f1",
                "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)

            d = response.json()
            context = {
                'city_name': city_name,
                'temperature': d.get('current').get('temp_c'),
                'text': d.get('current').get('condition').get('text')
            }

            return render(request, 'weather/weather.html', context)

        else:
            return render(request, 'weather/see_weather.html', {'form': form})


class WeatherView(View):
    def get(self, request, city_name):
        url = "https://weatherapi-com.p.rapidapi.com/current.json"

        querystring = {"q": f'{city_name}'}

        headers = {
            "X-RapidAPI-Key": "fa7da28988mshdfeb99f8717f94fp17da39jsn727e95c2c4f1",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        d = response.json()
        context = {
            'city_name': city_name,
            'temperature': d.get('current').get('temp_c'),
            'text': d.get('current').get('condition').get('text')
        }
        return render(request, 'weather/weather.html', context)


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "weather/register.html", context={"form": form})

    def post(self, request):
        create_form = UserRegisterForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect("login-page")
        else:
            context = {
                "form": create_form
            }
            return render(request, "weather/register.html", context=context)


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "weather/login.html", context={"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You have logged in as {username}")
                return redirect("home_page")
            else:
                messages.error(request, "Invalid username or password")
        else:
            return render(request, "weather/login.html", {"form": form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "User successfully loged out")
        return redirect("home_page")


class AddWeatherView(View):
    def get(self, request):
        form = AddWeatherForm(data=request.GET)
        return render(request, 'weather/add_city_weather.html', context={"form": form})

    def post(self, request):
        form = AddWeatherForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Weather added successfully!')
            return redirect('weather_list')
        else:
            return render(request, 'weather/add_city_weather.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        queryset = User.objects.get(username=request.user.username)
        return render(request, 'weather/profile.html', {'user': queryset})


class UpdateUserView(View):
    def get(self, request, **kwargs):
        user = User.objects.get(pk=kwargs["pk"])
        form = UserUpdateForm(instance=user)
        return render(request, 'weather/update_user.html', {'form': form})

