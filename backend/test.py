import requests

url = "http://127.0.0.1:5000/analyze"

payload = {
    "url": "https://example.com"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())