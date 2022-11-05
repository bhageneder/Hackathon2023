import requests

url = "https://target-com-shopping-api.p.rapidapi.com/product_fulfillment"

querystring = {"tcin":"51952757","longitude":"-122.200","store_id":"3330","state":"CA","zip":"94611","latitude":"37.820"}

headers = {
	"accept": "application/json",
	"cache-control": "no-cache",
	"authority": "redsky.target.com",
	"accept-language": "en-US,en;q=0.9",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)