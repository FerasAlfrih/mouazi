from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import View


class UserV(View):
    """docstring for UserV."""

    def __init__(self, arg):
        super(UserV, self).__init__()
        self.arg = arg

    @staticmethod
    def register(request):
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'users/register.html', context)
