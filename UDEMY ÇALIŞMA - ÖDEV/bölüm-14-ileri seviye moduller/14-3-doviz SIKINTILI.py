"""
Proje 3
https://www.doviz.com/ sitesinden anlık olarak doların,euronun,altının ve borsanın değerlerini öğrenin 
ve bunları kullanarak bir proje geliştirmeye çalışın.

Not: Bu projeyi, requests ve beautifulsoup kullanarak geliştirin.
"""

import requests

import sys
url = "https://www.doviz.com/"

birinci_doviz = input("Birinci Döviz:")
ikinci_döviz = input("İkinci Döviz:")
miktar = float(input("Miktar:"))


response = requests.get(url)

json_verisi = response.json()

print(json_verisi)


