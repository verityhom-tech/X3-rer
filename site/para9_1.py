import urllib.request

opener = urllib.request.build_opener()
req = urllib.request.Request("https://httpbin.org/get")
print(opener.open(req).read())