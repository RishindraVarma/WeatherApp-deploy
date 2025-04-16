import requests
from django.shortcuts import render


def index(request):
    weather_data = {}
    if request.method == "POST":
        city = request.POST.get('city')
        print(f"City entered: {city}")  # Debug log

        api_key = '33e2d49fe3c0cf0ca82c217b974f8b1a'
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        print(f"API Response Code: {response.status_code}")  # Debug log
        print(f"API Response Text: {response.text}")  # Debug log

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
            }
        else:
            weather_data['error'] = "City not found"

    return render(request, 'weather/index.html', {'weather_data': weather_data})
