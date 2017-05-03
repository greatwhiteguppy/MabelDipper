# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from models import User, Task
from datetime import datetime
import datetime
from django.contrib.auth import logout
from django.contrib import messages
from django.utils import timezone


# Create your views here.
def appointments(request):
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    context = {
    'today_tasks': Task.objects.filter(task_date__range=(today_min, today_max)),
    'other_tasks': Task.objects.all()
    }
    return render(request, "gravity_falls/appointments.html", context)

def addtask(request):
    print "In addtask mode"
    if request.method == "POST":
        print "request.POST:", request.POST
        valid, data = Task.objects.validate_create_task(request.POST)

        if valid == True:
            print "New successful task"
            messages.add_message(request, messages.SUCCESS, "new task added!")
            return redirect ("/appointments")

        else:
            for err in data:
                messages.error(request,err)
            return redirect ("/appointments")
    # # using ORM
    # Task.objects.create(task_name=request.POST['task_name'], task_date=request.POST['task_date'], task_time=request.POST['task_time'])
    # # insert into task (name, date, time, created_at, updated_at) values (name, date, time)
    # return redirect ('/appointments')

def remove(request, id):
    print "Removing a task!"
    if request.method == "POST":
        print request.POST
        deleted_task = Task.objects.get(id=id)
        print "This is the task we deleted:", deleted_task.id, "-", deleted_task.task_name

        deleted_task.delete()
        return redirect('/appointments')

def edit(request, id):
    print "Going to the edit page"
    if request.method == "GET":
        print request.GET
        context = {
            "task": Task.objects.get(id=id),
        }
    return render(request, "gravity_falls/edit.html", context)

def logout_view(request):
    print "Logging out of the app"
    logout(request)
    return redirect("/")
