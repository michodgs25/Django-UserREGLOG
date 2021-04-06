from django.shortcuts import render
from myapp.forms import LoginForm


def login(request):
    username = "not logged in"

    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
        else:
            MyLoginForm = Loginform()
            return render(request, 'loggedin.html', {"username": username})
