from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'registration/index.html')

def register(request):
    if request.method == 'Get'
        return redirect ('/')
    user = User.userManager.validate(request.POST['first_name'], request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['confirm_password'],)


    return redirect('/')

def logout(request):
    if 'userid' not in request.session:
        return redirect('/')
    del request.session['userid']
    return redirect('/')

def delete(request, id):
    if 'userid' not in request.session:
        return redirect('/')
    User.userManager.filter(id=id).delete()
    return redirect('/logout')
#
