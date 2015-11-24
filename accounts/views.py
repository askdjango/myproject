from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login as auth_login
from .forms import QuizAuthenticationForm, UserEmailCreationForm


def login(request):
    return auth_login(request, authentication_form=QuizAuthenticationForm)


def signup(request):
    if request.method == 'POST':
        form = UserEmailCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserEmailCreationForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })
