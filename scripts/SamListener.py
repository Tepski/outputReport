from listener import PLCListener
import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
import time

instance = PLCListener("192.168.1.253", 8500)

'''
ds_ok = X10
ns_pk = x16
ds_ng = X252
ns_ng =X254
ds_ok_arr = X200 - X222
ds_ng_arr = X201 - X223
ns_ok_arr = X224 -X246
ns_ng_arr = X225 - X247

'''

def ListenToSAMS(machine: int):
    retries = 0

    while True:

        reset = instance.read_val(f"R12{machine}02")
        print(f"SAM {machine}", reset.strip())

        if reset.strip() == "1":
            while retries != 3:
                try:
                    data = {
                        "machine": machine,
                        "date": str((datetime.now() + timedelta(days=1)).date()),
                        "ds_ok_count": instance.read_val(f"DM{machine}400"),
                        "ns_ok_count": instance.read_val(f"DM{machine}401"),
                        "ds_ng_count": instance.read_val(f"DM{machine}402"),
                        "ns_ng_count": instance.read_val(f"DM{machine}403"),
                        "ds_ok_perhr": str([int(instance.read_val(F"DM{machine}{x}").strip()) for x in range(404, 416)]),
                        "ds_ng_perhr": str([int(instance.read_val(f"DM{machine}{x}").strip()) for x in range(416, 428)]),
                        "ns_ok_perhr": str([int(instance.read_val(f"DM{machine}{x}").strip()) for x in range(428, 440)]),
                        "ns_ng_perhr": str([int(instance.read_val(f"DM{machine}{x}").strip()) for x in range(440, 452)])
                    }

                    res = requests.post(url="http://localhost:8000/api/addData/", json=data)

                    print(f"FROM SAM {machine}", res.status_code)

                    instance.reset(f"R12{machine}02")
                    print("Reset Success")

                    retries = 0

                    break
                except Exception as e:
                    retries += 1
                    print(f"Failed due to something: SAM {machine}")
                    print(f"SAM {machine}: {e}")
                    instance.reset(f"R12{machine}02")
                    print("Reset Success")

        time.sleep(1)

def main():
    with ThreadPoolExecutor() as executor:
        for sam in range(1, 9):
            executor.submit(ListenToSAMS, sam)

main()

