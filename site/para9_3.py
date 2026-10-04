import requests

response = requests.post("https://httpbin.org/post", "test post data", headers={"h1": "test-title"})
print(response.text)
