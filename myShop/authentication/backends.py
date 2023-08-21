from django.contrib.auth.backends import BaseBackend
from .models import User


class MyBackend(BaseBackend):
    def authenticate(self, request, phone=None, password=None):
        try:
            user = User.objects.get(phone=phone)
            if user.check_password(password) and getattr(user, "is_active", True):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
