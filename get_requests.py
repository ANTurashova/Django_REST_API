import requests

r = requests.get('http://127.0.0.1:8000/api/notes/')
print(r.text)
print(r.json())
print(r.status_code)

