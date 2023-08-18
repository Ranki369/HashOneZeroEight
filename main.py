import requests
import json

test_file = open("/resources/other_layer.json")
json_data = json.load(test_file)
headers =  {"Content-Type":"application/json"}
print("JSON string = ", json_data)
api_url = "https://hooks.slack.com/services/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"
test_response = requests.post(api_url, data=json.dumps(json_data), headers=headers)

if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
else:
    print("Something went wrong!")
  
print("hello python - requests executed")
