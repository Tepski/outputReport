from firebase import db
from google.cloud.firestore_v1 import FieldFilter
import requests, ast

res = requests.get("http://localhost:8000/api/getJSON/")

# doc_ref = db.collection("DATA").get()

# # for data in res.json():
# #     if len(str(data['date'])) > 10:
# #         print(data['date'][:10])
# #        .document(str(data['machine']) + "-SAM" + str(data['date'])[:10]).set(data, merge=True)

# for doc in doc_ref:
#     ds = ast.literal_eval(doc.to_dict()['ds_ok_perhr'])
#     ns = ast.literal_eval(doc.to_dict()['ns_ok_perhr'])

#     if sum(ds) == 0 and sum(ns) != 0:
#         data = {
#             'date': doc.to_dict()['date'],
#             'id': doc.to_dict()['id'],
#             'ns_ng_count': doc.to_dict()['ns_ng_count'],
#             'ns_ng_perhr': doc.to_dict()['ns_ng_perhr'],
#             'ns_ok_count': doc.to_dict()['ns_ok_count'],
#             'ns_ok_perhr': doc.to_dict()['ns_ok_perhr'],
#             'machine': doc.to_dict()['machine'],
#             'timestamp': doc.to_dict()['timestamp'],
#             'updated': doc.to_dict()['updated'],
#         }

#         db.collection("MachineData").document(doc.to_dict()["date"][:10] + "-SAM" + str(doc.to_dict()["machine"])).set(data, merge=True)
#         continue
#     elif sum(ns) == 0 and sum(ds) != 0:
#         data = {
#             'date': doc.to_dict()['date'],
#             'id': doc.to_dict()['id'],
#             'ds_ng_count': doc.to_dict()['ds_ng_count'],
#             'ds_ng_perhr': doc.to_dict()['ds_ng_perhr'],
#             'ds_ok_count': doc.to_dict()['ds_ok_count'],
#             'ds_ok_perhr': doc.to_dict()['ds_ok_perhr'],
#             'machine': doc.to_dict()['machine'],
#             'timestamp': doc.to_dict()['timestamp'],
#             'updated': doc.to_dict()['updated'],
#         }

#         db.collection("MachineData").document(doc.to_dict()["date"][:10] + "-SAM" + str(doc.to_dict()["machine"])).set(data, merge=True)
#         continue
#     elif sum(ds) != 0 and sum(ns) != 0:
#         data = doc.to_dict()
#         db.collection("MachineData").document(doc.to_dict()["date"][:10] + "-SAM" + str(doc.to_dict()["machine"])).set(data, merge=True)
#         continue

data = {"name": "SampleName", "age": 29}

print(data.keys())