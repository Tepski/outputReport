from listener import PLCListener
# string = ""
# hrly = ["ds_output", "ds_output"]

# for hr in hrly:
#     for i in range(24):
#         string += f' + "%2c" + STR({hr}[{i}])'

# print(string)

instance = PLCListener("192.168.1.253", 8500)

print(instance.read_val("R12402"))

# res = instance.read_val("R100").strip()

# '''
# ds_ok = X10
# ns_ok = x16
# ds_ng = X252
# ns_ng =X254
# ds_ok_arr = X200 - X222
# ds_ng_arr = X201 - X223
# ns_ok_arr = X224 -X246
# ns_ng_arr = X225 - X247

# data_location = X400    
# '''

# for i in range(1, 10):
#     lead = f"{i}00"
#     if i == 1:
#         lead = f"{i}05"
#     if i > 5:
#         lead = f"5{i}0"

#     print(f"""
# DM{i}400 = DM{lead}10
# DM{i}401 = DM{lead}16
# DM{i}402 = DM{i}252
# DM{i}403 = DM{i}254""")
    
#     ok_arr1 = [f"DM{i}{404 + x} = DM{i}{200 + (x * 2)}" for x in range(12)]
#     ng_arr1 = [f"DM{i}{416 + x} = DM{i}{201 + (x * 2)}" for x in range(12)]
#     ok_arr2 = [f"DM{i}{428 + x} = DM{i}{224 + (x * 2)}" for x in range(12)]
#     ng_arr2 = [f"DM{i}{440 + x} = DM{i}{225 + (x * 2)}" for x in range(12)]

#     for list in [ok_arr1, ng_arr1, ok_arr2, ng_arr2]:
#         for data in list:
#             print(data)
