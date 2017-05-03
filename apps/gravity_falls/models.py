# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from ..login_app.models import User
from django.db import models
import datetime

# Create your models here.
class TaskManager(models.Manager):
    def validate_create_task(self,data):
        print data, "validation and task data"

        errors = []

        if len(data["task_name"]) < 1:
            print "Task cannot be blank"
            errors.append("Task cannot be blank")
        if len(data["task_date"]) < 1:
            print "Task date must be filled in"
            errors.append("Task date must be filled in")
        if len(data["task_time"]) < 1:
            print "Task time must be filled in"
            errors.append("Task time must be filled in")
        # if data["task_date"] < datetime.date.today():
        #     print "Date cannot be in the past"
        #     errors.append("Date cannot be in the past")
        # if data["task_time"] < datetime.time.today():
        #     print "Time cannot be in the past"
        #     errors.append("Time cannot be in the past")
        if errors:
            return (False, errors)
        else:
            new_object = Task.objects.create(
                task_name = data["task_name"],
                task_date = data["task_date"],
                task_time = data["task_time"],
            )
            return (True, new_object)

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_date = models.DateField(auto_now=False)
    task_time = models.TimeField(auto_now=False)
    task_status = models.CharField(max_length=100, default="Pending")
    task_user = models.ForeignKey(User, related_name="usertasks", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TaskManager()
