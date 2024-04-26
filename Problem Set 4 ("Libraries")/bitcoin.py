from sys import argv, exit
import requests

if len(argv) != 2:
   exit("Usage: python bitcoin.py number_of_bitcoins")
try:
   n = float(argv[1])
except ValueError:
   exit("Usage: python bitcoin.py number_of_bitcoins")
try:
   file = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
   file_json = file.json()
   rate = file_json["bpi"]["USD"]["rate_float"]


except requests.RequestException:
   exit("sth wrong with the request")

price = n * rate
print(f"${price:,.4f}")

"""
{/////
"bpi":{
	"USD":{"code":"USD","symbol":"&#36;","rate":"28,984.2391","description":"United States Dollar","rate_float":28984.2391},
	"GBP":{"code":"GBP","symbol":"&pound;","rate":"24,218.9983","description":"British Pound Sterling","rate_float":24218.9983},
	"EUR":{"code":"EUR","symbol":"&euro;","rate":"28,234.8806","description":"Euro","rate_float":28234.8806}}
}
"""