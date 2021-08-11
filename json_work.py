# import urllib.request as ur
# import json
#
# json_url = input("Enter location: ")
# print("Retrieving:", json_url)
# data = ur.urlopen(json_url).read().decode('utf-8')
# print('Retrieved', len(data), 'characters')
# json_obj = json.loads(data)
#
# total = 0
# total_count = 0
#
# for comment in json_obj["comments"]:
#     total += int(comment["count"])
#     total_count += 1
#
# print('Count:', total_count)
# print('Sum:', total)


import json
import urllib.request as ur
import urllib.parse as up

service_url = "http://py4e-data.dr-chuck.net/json?"

address = input("Enter location: ")
params = {"key": "42", "address": address}
url = service_url + up.urlencode(params)
print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print("Place id", place_id)
