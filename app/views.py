from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from openpyxl import load_workbook
import os
from django.conf import settings
from io import BytesIO
from rest_framework.decorators import api_view
from rest_framework.response import Response

"""
AWS ROOT PASSWORD: {PC Password} + 01
"""

def handleExcel(data):
    try:
        excel_path = os.path.join(settings.BASE_DIR, "static", "TEMPLATE.xlsx")
        wb = load_workbook(excel_path)
        ws =  wb.active

        ws["A1"].value = data

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