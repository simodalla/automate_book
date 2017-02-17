import requests

r = requests.get('http://ip.jsontest.com')
print("Response object: ", r)
print("Response test: ", r.text)

payload = {'q': 'chetan'}
r = requests.get('https://github.com/search', params=payload)
print("Request URL: ", r.url)

payload = {'key1': 'value1'}
r = requests.post('https://httpbin.org/post', params=payload)
print("Request text: ", r.json())

try:
    r = requests.get('http://www.googleFAKE.com')
except requests.exceptions.RequestException as e:
    print("Error Response: ", e.message)
