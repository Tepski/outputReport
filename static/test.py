import requests

for i in range(1, 9):
    url = f"https://outputreport.onrender.com/api/deleteData/{i}/"

    res = requests.delete(url)

    print(res)