# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from .forms import MainForm
from .utils import predict_price
def index(request):
    result = ""
    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            est_price = predict_price(data['district'],data['rooms'],data['furnished'],data['meters'])
            result = f"Estimated price: {est_price} PLN"
    else:
        form = MainForm()

    return render(request, "forms/index.html",context={"form":form,"result":result})