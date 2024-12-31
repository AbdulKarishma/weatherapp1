from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
    # Default city
    city = 'indore'

    # Check if city is entered in the form
    if request.method == 'POST':
        city = request.POST.get('city', 'indore')  # Get user-input city

    # OpenWeatherMap API URL with city and app ID
    API_KEY = '886a990225a718e70e402a3207226e45'  # Replace with your actual API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    PARAMS = {'units': 'metric'}

    try:
        # Fetch weather data
        response = requests.get(url, PARAMS)
        data = response.json()

        # Check if response is valid
        if response.status_code == 200:
            # Extract weather details
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
            temp = data['main']['temp']
        else:
            # Handle invalid city name
            description = "City not found!"
            icon = "01d"  # Default icon
            temp = "N/A"
            city = "Unknown"

    except Exception as e:
        # Handle network/API errors
        description = "Unable to fetch data. Please try again later."
        icon = "01d"  # Default icon
        temp = "N/A"
        city = "Unknown"

    # Get today's date
    day = datetime.date.today()

    # Render template with weather data
    return render(request, 'index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city,
    })
