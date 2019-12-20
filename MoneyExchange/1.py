import pycbrf
import datetime
q = datetime.datetime.date(datetime.datetime.today())
rates = pycbrf.ExchangeRates(q, locale_en=False)
a = rates.rates
for i in a:
    print(i[3])