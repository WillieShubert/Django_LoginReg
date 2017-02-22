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
        'user' : User.objects.get(id=request.session['userid'])
    }
    print context['user'].first_name
    return render(request, 'registration/success.html', context)

def register(request):
    if request.method == 'GET':
        return redirect ('/')
    newuser = User.objects.validate(request.POST)
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
    # if 'userid' in request.session:
    #     return redirect('/success')
    if request.method == 'GET':
        return redirect('/')
    else:
        user = User.objects.login(request.POST)
        print user
        if user[0] == False:
            for each in user[1]:
                messages.add_message(request, messages.INFO, each)
            return redirect('/')
        if user[0] == True:
            messages.add_message(request, messages.INFO,'Welcome, You are logged in!')
            request.session['userid'] = user[1].id
            return redirect('/success')


def logout(request):
    if 'userid' not in request.session:
        return redirect('/')
    print "*******"
    print request.session['userid']
    del request.session['userid']
    return redirect('/')

#
# def logout_view(request):
#     logout(request)
#     return redirect('/')
#
# def login_view(request):
#     if request.method == 'GET':
#         return redirect('/')
#     if 'userid' in request.session:
#         return redirect('/success')
#     email = request.POST['email']
#     password = request.POST['password']
#     user = authenticate(email=email, password=password)
#     if user is not None:
#         login(request, user)
#         messages.success(request, 'Welcome, You are logged in!')
#         return redirect('/success')
#     else:
#         messages.errors(request, each)
#         return redirect('/')
#
#
# def login(request):
#     if 'userid' in request.session:
#         return redirect('/success')
#     if request.method == 'GET':
#         return redirect('/')
#     user = User.objects.login(request.POST['email'], request.POST['password'])
#     print user
#     if user[0] == False:
#         for each in user[1]:
#             messages.errors1(request, each)
#         return redirect('/')
#     if user[0] == True:
#         messages.success(request, 'Welcome, You are logged in!')
#         request.session['userid'] = user[1].id
#         return redirect('/success')





# def delete(request, id):
#     if 'userid' not in request.session:
#         return redirect('/')
#     User.objects.filter().delete()
#     return('/logout')
