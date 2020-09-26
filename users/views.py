from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    View
)


class Registration(CreateView):
    template_name = "registration/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("users:login")


class ProfileUpdate(LoginRequiredMixin, View):
    template_name = "registration/profile.html"

    def get(self, request, *args, **kwargs):
        context = {}
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context["u_form"] = u_form
        context["p_form"] = p_form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("users:profile")
