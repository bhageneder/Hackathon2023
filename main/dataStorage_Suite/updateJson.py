import json
 
#Initialize dict object to store json data
dictionary = {}

#Method to determine if a list is empty
def isEmpty(array):
    if not array:
        return True
    else:
        return False

 
def obtain_json(json_name, data_to_be_written):
    while(not data_to_be_written.isEmpty()):
        dictionary.update()
    


    
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)