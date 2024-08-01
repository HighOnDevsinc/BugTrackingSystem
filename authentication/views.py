from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate # noqa
from django.views.generic import TemplateView, View
from .forms import SignUpForm, SignInForm


class HomeView(TemplateView):
    template_name = 'home.html'


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'sign_up.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'sign_up.html', {'form': form})


class SignInView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'sign_in.html', {'form': form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = SignInForm(request.POST)
            form.add_error(None, 'Invalid username or password')
            return render(request, 'sign_in.html', {'form': form})


class SignOutView(TemplateView):
    template_name = 'sign_out.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')