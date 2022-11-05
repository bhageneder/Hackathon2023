import requests

url = "https://target-com-shopping-api.p.rapidapi.com/product_search"

querystring = {"store_id":"1122","keyword":"womens shoes","offset":"0","count":"25"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)