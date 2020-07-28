from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from .forms import UserRegisterForm


class UsersV(View):
    """docstring for UserV."""

    def __init__(self, arg):
        super(UserV, self).__init__()
        self.arg = arg

    @staticmethod
    def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(
                    request, f'Your account has been created! You are now able to log in')
                return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
