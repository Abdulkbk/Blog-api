from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):
  def create_user(self, email, password, name, **extra_fields):
    
    if not email:
      raise ValueError('User must have an email')

    user = self.model(
      email = self.normalize_email(email),
      name=name, 
      **extra_fields
    )


    user.set_password(password)

    user.save()

    return user

  def create_superuser(self, email, password, name, **extra_fields):

    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    return self.create_user(email, password, name, **extra_fields)
    

   



class CustomUser(AbstractBaseUser, PermissionsMixin):

  email = models.EmailField(verbose_name='email address', unique=True, max_length=255)

  name = models.CharField(max_length=255)

  date_joined = models.DateTimeField(default=timezone.now)

  is_staff = models.BooleanField(default=False)

  is_active = models.BooleanField(default=True)

  is_superuser = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  objects = UserManager()

  def __str__(self) -> str:
      return self.name


