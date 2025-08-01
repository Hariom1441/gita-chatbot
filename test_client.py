import requests

url = "http://127.0.0.1:5000/ask"
payload = {"question": "What is karma?"}
response = requests.post(url, json=payload)

print("GitaBot:", response.json().get("response"))
