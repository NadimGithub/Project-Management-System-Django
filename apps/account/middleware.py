# myapp/middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            if not request.path.startswith(reverse('login')) and not request.path.startswith(reverse('register')):
                return redirect(settings.LOGIN_URL)
