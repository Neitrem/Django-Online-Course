from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset
from django.template import loader

import json




def index(request):
    return render(request, 'main/index.html')