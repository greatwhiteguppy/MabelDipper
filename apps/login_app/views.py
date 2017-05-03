# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from models import User
import bcrypt

# Create your views here.
def index(request):
    if "id" in request.session:
        context = {
            "users": User.objects.GetUser(request.session["id"])
        }
        return render(request, "login_app/index.html", context)

    print "In index"

    if request.method == "GET":
        return render(request, "login_app/index.html")


def register(request):
    print "In registration"
    if request.method == "POST":
        print "request.POST:", request.POST
        valid, data = User.objects.validate_and_create(request.POST)

        if valid == True:
            print "New successful registration"
            messages.add_message(request, messages.SUCCESS, "registered!")

        else:
            for err in data:
                messages.error(request,err)
            return redirect("/")

    user_info = User.objects.validate_and_login(request.POST)
    request.session["name"] = user_info[1].name

    return HttpResponseRedirect("appointments")


def login(request):
    print "In login"
    if request.method == "POST":
        print "request.POST:", request.POST
        valid, data = User.objects.validate_and_login(request.POST)

        if valid == True:
            print "Login complete"
            messages.add_message(request, messages.SUCCESS, "logged in!")
        else:
            for err in data:
                messages.error(request,err)
            return redirect("/")
    context = {
        "users": User.objects.all()
    }

    user_info = User.objects.validate_and_login(request.POST)
    request.session["name"] = user_info[1].name

    return HttpResponseRedirect("appointments", context)
