from django.contrib.sites import requests
from django.shortcuts import render
import requests
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request, 'index.html')


def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        API_KEY = '37323fbb8cd7eb495cc42f8f527cd341'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        # pip install requests
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)
            data1 = data['coord']
            data2 = data['wind']
            context = {'data': data, 'data1': data1, 'data2': data2}

            return render(request, 'index.html', context)
        else:
            return render(request, 'index.html')
