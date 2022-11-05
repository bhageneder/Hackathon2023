import requests

url = "https://target-com-shopping-api.p.rapidapi.com/autocomplete"

querystring = {"q":"tv"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

