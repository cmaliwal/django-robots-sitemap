# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import DataRow
from .forms import DataRowForm


def index(request):
    if request.method == 'POST':
        form = DataRowForm(request.POST)
        if form.is_valid():
            DataRow.objects.create(date=request.POST['date'], gender = request.POST['gender'], favorite_number = request.POST['favorite_number'])
            return redirect('/')
    else:
        form = DataRowForm()
    datarows=DataRow.objects.all()
    count = DataRow.objects.count()
    return render(request, 'index.html', {'data_row':datarows, 'count':count, 'form':form})
