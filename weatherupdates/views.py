from django.shortcuts import render, redirect
import requests
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import authenticate 
from django.contrib.auth import login as loginUser, logout as logoutuser
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required




def signup(request):
    if request.method=='GET':
        print("Hello Ramu")
        form = UserRegistrationForm()
        message = None
        context = {'form': form, 'message': message}
        return render(request, 'signup.html', context)
    else:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                loginUser (request, user)
                return redirect('home')
                
# pip install django-bootstrap-datepicker-plus
        else:
            expalnation = form.errors.as_data()
            for key in expalnation:
                for value in expalnation[key]:
                    message = value
                    if message is not None:
                        break
            form = UserRegistrationForm()
            context = {'form': form, 'message': message}
            return render(request, 'signup.html', context)


# the index() will handle all the app's logic
@login_required(login_url="login/")
def index(request):
    # if there are no errors the code inside try will execute
    try:
        # checking if the method is POST
        API_KEY = '4da85e50a9e8c8b0e38766bcdb4de4da'
        if request.method == 'POST':
            # getting the city name from the form input   
            city_name = request.POST.get('city')
            # the url for current weather, takes city_name and API_KEY   
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_KEY}'
            # url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={API_KEY}'

            # city = 'Las Vegas'

            # converting the request response to json   
            response = requests.get(url).json()
            # print(response)
            # getting the current time
            current_time = datetime.now()
            # formatting the time using directives, it will take this format Day, Month Date Year, Current Time 
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            # bundling the weather information in one dictionary
            cities_weather_update = [{
                'city': city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }]
           

            # if the request method is GET empty the dictionary
        else:
            CITIES=['Mumbai','Delhi','Bangalore','Hyderabad','Kolkata']
            
            cities_weather_update = []
            
            for city_name in CITIES:
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_KEY}'
                # url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={API_KEY}'

                # city = 'Las Vegas'

                # converting the request response to json   
                response = requests.get(url).json()
                # print(response)
                # getting the current time
                current_time = datetime.now()
                # formatting the time using directives, it will take this format Day, Month Date Year, Current Time 
                formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
                # bundling the weather information in one dictionary
                city_weather_update = {
                    'city': city_name,
                    'description': response['weather'][0]['description'],
                    'icon': response['weather'][0]['icon'],
                    'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                    'country_code': response['sys']['country'],
                    'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                    'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                    'time': formatted_time
                }

                


                cities_weather_update.append(city_weather_update)
                
            
        context = {'cities_weather_update': cities_weather_update}

        return render(request, 'weatherupdates/home.html', context)


    except Exception as e:
        print (e)
        return render(request, 'weatherupdates/404.html')



def login(request):
    if request.method=='GET':
        form=AuthenticationForm()
        context = {
            "form" : form
       }
        return render(request,'login.html', context=context)
    else:
        form=AuthenticationForm(data=request.POST)
        # print(form.is_valid())  
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request,'login.html', context=context)


def logout(request):
    logoutuser(request)
    return redirect('login')






