from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from accounts.forms import HeadSignupForm
from .models import User

class HeadSignupView(CreateView):
    model = User
    form_class = HeadSignupForm
    template_name = 'registration/signup-form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

