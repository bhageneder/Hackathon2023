import requests
import time
import os

url = "https://target-com-shopping-api.p.rapidapi.com/product_search"
rapidKey = '930401d6a5mshe61534d11163938p1ecd97jsn6a9d82d02d3d'

def productSearch(store_id, keyword, offset, count):
	inputquerystring = {"store_id":store_id,"keyword":keyword,"offset":offset,"count":count}
	querystring = {"store_id":"1122","keyword":"womens shoes","offset":"0","count":"1"}

	headers = {
		"X-RapidAPI-Key": rapidKey,
		"X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
	}

	inputresponse = requests.request("GET", url, headers=headers, params=inputquerystring)
	#expectedresponse = requests.request("GET", url, headers=headers, params=querystring)
	responseJSON = inputresponse.json()
	for event in responseJSON['data']:
		print(event['name'])
		print(event['id'])

	with open("sample.json", "w+") as outfile:
		outfile.writelines(responseJSON)

	#print("Actual Response: {}\n".format(inputresponse.json))


	#print("Expected Response: {}\n".format(expectedresponse.text[1:25]))

	return inputresponse

productSearch("1122","womens shoes","0","1")