from django.shortcuts import render
from django.http import FileResponse
from openpyxl import load_workbook
import os
from django.conf import settings
from io import BytesIO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import MachineSrlzr
from rest_framework import status
from .models import MachineData

"""
AWS ROOT PASSWORD: {PC Password} + 01
"""

def handleExcel(data):
    try:
        excel_path = os.path.join(settings.BASE_DIR, "static", "TEMPLATE.xlsx")
        wb = load_workbook(excel_path)
        ws =  wb.active

        ws["G1"].value = data["name"]
        ws["M1"].value = data["date"]
        #b5 b6 b8 b9
        ws["B5"].value = data["ds_ok"]
        ws["B6"].value = data["ds_ng"]
        ws["B8"].value = data["ns_ok"]
        ws["B9"].value = data["ns_ng"]

        output = BytesIO()
        wb.save(output)
        output.seek(0)

        return output
    except:
        print("An error occured")


def generate_excel(request):
    data = request.GET.get('value')

    res = handleExcel(data)

    return FileResponse(res, as_attachment=True, filename="TestFile.xlsx")

@api_view(["POST"])
def setData(request):
    res = request.data
    srlzr = MachineSrlzr(data=res)
    if srlzr.is_valid():
        srlzr.save()

        return Response(srlzr.data, status=status.HTTP_200_OK)
    
    return Response({"Message": "Failed"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def getData(request, machine):
    data = MachineData.objects.get(machine=machine)
    srlzr = MachineSrlzr(data)
    dict = {
        "name": f"SAM {srlzr.data['machine']}",
        "date": srlzr.data["date"],
        "ds_ok": srlzr.data["ds_ok_count"],
        "ds_ng": srlzr.data["ds_ng_count"],
        "ns_ok": srlzr.data["ns_ok_count"],
        "ns_ng": srlzr.data["ns_ng_count"],
        "ds_ok_hr": srlzr.data["ds_ok_perhr"],
        "ds_ng_hr": srlzr.data["ds_ng_perhr"],
        "ns_ok_hr": srlzr.data["ns_ok_perhr"],
        "ns_ng_hr": srlzr.data["ns_ng_perhr"]
    }

    res = handleExcel(dict)
    
    return FileResponse(res, as_attachment=True, filename=f"{dict['name']}.xlsx")