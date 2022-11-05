import requests
import time

url = "https://target-com-shopping-api.p.rapidapi.com/product_search"
rapidKey = 'null'

def productSearch(store_id, keyword, offset, count):
	inputquerystring = {"store_id":store_id,"keyword":keyword,"offset":offset,"count":count}
	querystring = {"store_id":"1122","keyword":"womens shoes","offset":"0","count":"1"}

	headers = {
		"X-RapidAPI-Key": rapidKey,
		"X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
	}

	inputresponse = requests.request("GET", url, headers=headers, params=inputquerystring)
	#expectedresponse = requests.request("GET", url, headers=headers, params=querystring)

	#print("Actual Response: {}\n".format(inputresponse.text))


	#print("Expected Response: {}\n".format(expectedresponse.text[1:25]))

	return inputresponse

productSearch("1122","womens shoes","0","1")