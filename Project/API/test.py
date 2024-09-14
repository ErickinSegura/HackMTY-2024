import requests

url = 'https://redesigned-space-succotash-v9wv45jjqxw3pvpv-5000.app.github.dev/prompt'

# Send POST to /echo with "hello" prompt and selection 2
data = {"prompt": "hello", "selection": 2}
response = requests.post(url, json=data)
print(response.text)
