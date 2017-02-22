from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'registration/index.html')

def success(request):
    if 'userid' not in request.session:
        return redirect ("/")
    context = {
        'user' : User.objects.get(id= request.session['userid'])
    }
    print context['user'].first_name
    return render(request, 'registration/success.html', context)

def register(request):
    if request.method == 'GET':
        return redirect ('/')
    newuser = User.objects.validate(request.POST['first_name'], request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['confirm_password'])
    print newuser
    if newuser[0] == False:
        for each in newuser[1]:
            messages.error(request, each)
        return redirect('/')
    if newuser[0] == True:
        messages.success(request, 'Well done')
        request.session['userid'] = newuser[1].id
        return redirect('/success')

def login(request):
    if request.method == 'GET':
        return redirect('/')
    user = User.objects.login(request.POST['email'], request.POST['password'])
    print user
    if user[0] == False:
        for each in user[1]:
            messages.errors1(request, each)
        return redirect('/')
    if user[0] == True:
        messages.success(request, 'Welcome, You are logged in!')
        request.session['userid'] = user[1].id
        return redirect('/success')


def logout(request):
    if 'userid' not in request.session:
        return redirect('/')
    # if not request.user.is_authenticated:
    #     return redirect('/')
    del request.session['userid']
    return redirect('/')

def delete(request, id):
    if 'userid' not in request.session:
        return redirect('/')
    User.objects.filter().delete()
    return('/logout')
