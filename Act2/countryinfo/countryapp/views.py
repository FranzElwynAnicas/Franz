import requests
from django.shortcuts import render

def get_country_info(request):
    country_data = None
    error_message = None
    country = request.GET.get('country')

    if country:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
        if response.status_code == 200:
            country_data = response.json()[0]  # Get the first matching result
        else:
            error_message = "Country not found. Please try again."

    return render(request, 'country.html', {'country': country_data, 'error_message': error_message})
