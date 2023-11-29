# marksheet_app/urls.py
from django.urls import path
from .views import marksheet, add_student

urlpatterns = [
    path('marksheet/', marksheet, name='marksheet'),
    path('add_student/', add_student, name='add_student'),
]
