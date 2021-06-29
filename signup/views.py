from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import UserCreateForm
from .models import UserDetail


def index(requests):
    form = UserCreateForm()
    if requests.method == "POST":
        form = UserCreateForm(requests.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            return redirect('blog:index')
    context = {
        'form': form,
    }
    return render(requests, 'signup/index.html', context)

# TODO: i need to pass the form.cleaned_data to the template so the user's username can be refrenced when
#   the form for logging in shows.
