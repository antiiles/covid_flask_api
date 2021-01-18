import requests
res = requests.post('http://localhost:5000/api/echo-json', json={"donkeu":"DK"})
if res.ok:
    print(res.json())