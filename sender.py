import requests

# response = requests.get('http://127.0.0.1:5000')
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.text)

response = requests.post(
    'http://127.0.0.1:5000/send',
    json={'name': 'Name', 'text': '123'}
)
print(response)
