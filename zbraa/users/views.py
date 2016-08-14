# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from allauth.account.views import PasswordChangeView

from .models import User

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False
    def get_redirect_url(self):
        return reverse("theme:home")


class UserUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported User in the view code above, remember?
    model = User
    fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'residence',
        ]

    # send the user back to their own page after a successful update
    success_url = reverse_lazy("users:update")

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)

class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

# ============================================================================

class BackendPasswordChanged(PasswordChangeView):
    success_url = reverse_lazy("users:list")
