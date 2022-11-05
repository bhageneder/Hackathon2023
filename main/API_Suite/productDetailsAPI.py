import requests

url = "https://target-com-shopping-api.p.rapidapi.com/product_details"

querystring = {"tcin":"16251811","store_id":"3330","longitude":"-122.200","latitude":"37.820","zip":"94611","state":"CA"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
