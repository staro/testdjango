from django.shortcuts import render


def index(request):
    return render(request, 'account/index.html')


def signin(request):
    return render(request, 'account/signin.html')


def signup(request):
    return render(request, 'account/signup.html')

def signout(request):
    return render(request, 'account/signout.html')


def pass_reset(request):
    return render(request, 'account/pass_reset.html')


def settings(request):
    return render(request, 'account/settings.html')
