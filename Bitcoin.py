#step1-open the URL for bit coin price data
#step2 install the python request library
#imports the requests library
import requests
#calls the get function on the requests library and passes in a URL as a parameter. It assigns what is returned to a variable called response.
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#calls the json() method on the response object we just created
data = response.json()
#prints the price data.
print(data["bpi"]["USD"]["rate"])
