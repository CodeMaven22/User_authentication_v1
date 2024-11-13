# authentication_backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Attempt to find user by email, student_id, or employment_id
            user = (User.objects.filter(email=username).first() or
                    User.objects.filter(student_id=username).first() or
                    User.objects.filter(lecturer_id=username).first() or
                    User.objects.filter(registrar_id=username).first())

            if user and user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
