from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, BaseUserManager,PermissionsMixin
#from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):

    def _create_user(self, email,user_name, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,user_name = user_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,email, user_name, password, **extra_fields):       # Fields which user have to fill while sgining up
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,user_name,user_name, password, **extra_fields)

    def create_superuser(self, email, user_name, password, **extrafields):
        extrafields.setdefault('is_staff',True)
        extrafields.setdefault('is_superuser',True)
        extrafields.setdefault('is_active', True)

        if extrafields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extrafields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email,user_name, password, **extrafields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    user_name = models.CharField(max_length=200, unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'    #Field that we want to use while login
    REQUIRED_FIELDS = ['user_name'] #Fields that we want while creating super user

    def __str__(self):
        return self.user_name
    