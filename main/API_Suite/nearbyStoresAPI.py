import requests

url = "https://target-com-shopping-api.p.rapidapi.com/nearby_stores"

querystring = {"place":"10010","limit":"20","within":"100"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)