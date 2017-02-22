from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
Email_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
Name_Regex = re.compile(r'^[A-Za-z]+$')

# Create your models here.
class userManager(models.Manager):
    def validate (self, postFirstName, postLastName, postEmail, postPassword, postConfirm):
        errors = []
        if not Email_Regex.match(postEmail):
            errors.append("Invalid email")
        if len(User.objects.filter(email = postEmail)) > 0:
            errors.append("Email already exists in our database")
        if postPassword != postConfirm:
            errors.append("Your passwords don't match")
        if len(postFirstName) < 2:
            errors.append("Is that really your first name?")
        if len(postLastName) < 2:
            errors.append("Is that really your last name?")
        if not Name_Regex.match(postFirstName):
            errors.append("Is that number really in your first name?")
        if not Name_Regex.match(postLastName):
            errors.append("Is that number really in your first name?")
        if len(postPassword) < 8:
            errors.append("Password too short")
        if len(errors) == 0:
            password = postPassword
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            #create the user
            newuser = User.objects.create(first_name= postFirstName, last_name= postLastName, email= postEmail, password= hashed)
            return (True, newuser)
        else:
            return (False, errors)


    def login(self, postEmail, postPassword):
        errors1 = []
        user = User.objects.filter(email = postEmail)

        if not Email_Regex.match(postEmail):
            errors1.append("Invalid email")
        elif len(postPassword) < 8:
            errors1.append("Password too short")
            return (False, errors1)

        if len(errors1) == 0: #if we have no errors..
            if bcrypt.hashpw(postPassword.encode(), user[0].password.encode()) == user[0].password:
                return (True, user )

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()
