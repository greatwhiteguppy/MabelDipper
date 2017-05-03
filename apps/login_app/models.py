# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

EMAIL_REGEX =re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

LETTERS_ONLY = re.compile(r'[A-Za-z]')

# Create your models here.
class UserManager(models.Manager):
    def validate_and_create(self,data):
        print data, "validation and database data"

        repeat_email = User.objects.filter(email=data['email'])
        errors = []
    # validate name info
        if len(data['name']) < 2:
            print "Name must be at least 2 characters"
            errors.append("Name must be at least 2 characters")
        if not LETTERS_ONLY.match(data['name']):
            print "Name must contain letters only"
            errors.append("Name must contain letters only")
    # validate email info
        if len(data['email']) < 1:
            print "Email cannot be blank"
            errors.append("Email cannot be blank")
        if not EMAIL_REGEX.match(data['email']):
            print "Email is not valid"
            errors.append("Email is not valid")
        if len(repeat_email) > 0:
            print "Email has already been registered"
            errors.append("Email has already been registered")
    # validate password (at least 8 characters/ cannot be empty)
        if len(data['password']) < 8:
            print "Password must be at least 8 characters long"
            errors.append("Password must be at least 8 characters long")
    # validate password confirmation(match password)
        if data['password'] != data['confirm_password']:
            print "Passwords do not match"
            errors.append("Passwords do not match")
    # if email_entered == replicated.email:

        if errors:
            return (False, errors)
        else:
    # Bcrypt encryption
            pw = data['password']
            hashed_pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())

            new_object = User.objects.create(
                name = data['name'],
                email = data['email'],
                password = hashed_pw, #<---HASHED PASSWORD
                birthday = data['birthday'],
                )

            return (True, new_object)

    def validate_and_login(self,data):
        #validate email (valid email format/ cannot be empty)
        User_Exists = User.objects.filter(email=data['email'])
        print User_Exists, "<--- replicated"
        errors = []
        if len(data['email']) < 1:
            print "Email cannot be blank"
            errors.append("Email cannot be blank")
        if not EMAIL_REGEX.match(data['email']):
            print "Email is not valid"
            errors.append("Email is not valid")
        #Check to see if email address entered is in database
        if len(User_Exists) == 0:
            print "Email is not registered"
            errors.append("Email is not registered")
        #validate password (at least 8 characters/ cannot be empty)
        if len(data['password']) < 8:
            print "Password must be at least 8 characters long"
            errors.append("Password must be at least 8 characters long")
        if errors:
            return (False, errors)
        else:
            login_user = User.objects.get(email=data['email'])
            pw = data['password']

            # hashed_pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
            if bcrypt.hashpw(pw.encode(), login_user.password.encode()) == login_user.password.encode():
            # if bcrypt.checkpw(pw.encode(), login_user.password.encode()):
                print "the passwords match"
                return (True, login_user)
            else:
                print "the passwords don't match"
                errors.append("Invalid Password")
                return (False, errors)



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    birthday = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
