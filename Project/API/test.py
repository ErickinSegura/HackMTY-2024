import requests

url = 'https://redesigned-space-succotash-v9wv45jjqxw3pvpv-5000.app.github.dev/'

# Send POST to /echo with "hello"
data = {"prompt": "hello", "selection": 2}
response = requests.post(url + 'echo', json=data)
print(response.text)