import datetime
import decimal

from django.http import HttpResponse
from django.shortcuts import render
import pycbrf


def post(request):
    rates = pycbrf.ExchangeRates(datetime.datetime.date(datetime.datetime.today()), locale_en=False)
    return render(request, 'MoneyExchange/Exchange.html', {'rates': rates.rates})


def changeto(request):
    if request.method == 'GET':
        number = float(request.GET.get('number'))
        a = request.GET.get('from')
        b = request.GET.get('to')
        rates = pycbrf.ExchangeRates(datetime.datetime.date(datetime.datetime.today()), locale_en=False)
        #print(rates[a].value)
        return HttpResponse("{0:.2f}".format(number/float(rates[b].value)*float(rates[a].value)))
