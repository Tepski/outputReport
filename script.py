import requests

url = "http://outputreport.onrender.com/api/getJSON/"
dest = "http://127.0.0.1:8000/api/addData/"

res = requests.get(url)

data = res.json()

for datum in data:
    res = requests.post(dest, json=datum)

    print(res)