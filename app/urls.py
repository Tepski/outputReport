from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.generate_excel, name='ExcelFile'),
    path("addData/", views.setData, name="AddData"),
    path("getData/<int:machine>/", views.getData, name='GetData'),
    path("deleteData/<int:machine>", views.deleteData, name="DeleteData"),
    path("/", views.returnHomePage, name="HomePage")
    # path("getALlData/<str:date>", views.getAllData, name='GetAllData)
]
