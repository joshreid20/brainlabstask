import random

from django.shortcuts import render
from .forms import CountryGuesserForm
from django.contrib import messages
import requests

def main(request):
    if request.method == 'POST':
        form = CountryGuesserForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data['country']
            country_link = f'<a href="https://www.google.com/search?q={country.replace(" ", "+")}" target="_blank">{country}</a>'
            if form.cleaned_data['capital'].upper() == form.cleaned_data['correct_capital'].upper():
                messages.success(request, f'That is correct. The capital of {country_link} is indeed {form.cleaned_data["correct_capital"]}. Well done!')
            else:
                messages.error(request, f'That is incorrect. The capital of {country_link} is {form.cleaned_data["correct_capital"]}. Try the next one.')

    response_json = requests.get("https://countriesnow.space/api/v0.1/countries/capital").json()
    country_entry = response_json['data'][random.randint(0, len(response_json['data'])-1)]

    form = CountryGuesserForm()
    form.fields["correct_capital"].initial = country_entry['capital']
    form.fields["country"].initial = country_entry['name']

    context = {'form': form,
               'country': country_entry['name']}
    return render(request, 'capital_guesser.html', context)


