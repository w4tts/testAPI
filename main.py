import requests

r = requests.get("https://reqres.in/api/users")
print(r.text)

