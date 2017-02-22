from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
Email_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
Name_Regex = re.compile(r'^[A-Za-z]+$')

# Create your models here.
class userManager(models.Manager):
    def validate (self, postFirstName, postLastName, postEmail, postPassword, postConfirm):
        if not Email_Regex.match(postEmail):
            return {'errors':'False'}
        elif len(User.userManager.filter(email = postEmail)) > 0:
            return {'errors1': 'False'}
        elif postPassword != postConfirm:
            return {'errors2': 'False'}
        elif len(postFirstName) < 2:
            return {'errors3': 'False'}
        elif len(postLastName) < 2:
            return {'errors3': 'False'}
        elif not Name_Regex.match(postFirstName):
            return {'errors4': 'False'}
        elif not Name_Regex.match(postLastName):
            return {'errors4': 'False'}
        elif len(postPassword) < 8:
            return {'errors5': 'False'}
        else:
            password = postPassword
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return {'first_name': postFirstName, 'last_name': postLastName, 'email': postEmail, 'password': hashed}

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
