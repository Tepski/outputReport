from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.generate_excel, name='ExcelFile')
]
