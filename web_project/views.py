from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset

from .resources import EmployeeResource
from .models import Employee


