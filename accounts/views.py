from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm


def signup(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/accounts/login/')

    else:

        form = SignUpForm()

    return render(request, 'signup.html', {
        'form': form
    })

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/product/')

        else:

            error = 'Invalid username or password.'

            return render(request, 'login.html', {
                'error': error
            })

    return render(request, 'login.html')


def user_logout(request):

    logout(request)

    return redirect('/product/home/')


def account(request):

    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    return render(request, 'account.html')