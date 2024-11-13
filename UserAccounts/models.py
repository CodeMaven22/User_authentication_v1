from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required")

        # Check if the role and required IDs are provided
        role = extra_fields.get('role')
        if role == 'student' and not extra_fields.get('student_id'):
            raise ValueError("Student ID is required for students")
        elif role == 'lecturer' and not extra_fields.get('lecturer_id'):
            raise ValueError("Employment ID is required for staff and lecturers")
        elif role == 'registrar' and not extra_fields.get('registrar_id'):
            raise ValueError("Employment ID is required for staff and registrar")

        # Create user
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            raise ValueError('Password is required')

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    lecturer_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    registrar_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('registrar', 'registrar'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
