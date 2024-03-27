from django.contrib import admin
from django.urls import path


from weather.views import HomePageView, UserLoginView, UserLogoutView, UserRegisterView, SeeWeather, WeatherListView, \
    AddWeatherView, WeatherView, ProfileView, UpdateUserView

app_name = 'weather'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home_page'),
    path('login/', UserLoginView.as_view(), name='login_page'),
    path('logout/', UserLogoutView.as_view(), name='logout_page'),
    path('register/', UserRegisterView.as_view(), name='register_page'),
    path('profile/', ProfileView.as_view(), name='profile_page'),
    path('see_weather/', SeeWeather.as_view(), name='see_weather'),
    path('weather/<city_name>', WeatherView.as_view(), name='weather_'),
    path('user_update/<pk>', UpdateUserView.as_view(), name='update_user'),
    path('weather_list/', WeatherListView.as_view(), name='weather_list'),
    path('add_city_weather/', AddWeatherView.as_view(), name='add_city_weather')
]
