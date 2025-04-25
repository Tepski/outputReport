from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.generate_excel, name='ExcelFile'),
    path("addData/", views.setData, name="AddData"),
    path("getData/<int:machine>/", views.getData, name='GetData')
]
