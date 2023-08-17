import requests

test_file = open("small_msg.json", "rb")
test_url = "https://hooks.slack.com/services/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?Content-type=application/json"
test_response = requests.post(test_url, files = {"payload": test_file})

if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
else:
    print("Something went wrong!")
  
print("hello python")
