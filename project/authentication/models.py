from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        if not password:
            raise ValueError('Password is required')

        try:
            user = self.model( email=self.normalize_email(email), **extra_fields)
            user.set_password(password)
            user.save()
            return user
        except:
            raise ValueError('Please try again')


    def create_superuser(self, email, password=None, **extra_fields):
        try:
            user = self.create_user(email, password=password, is_admin=True, is_superuser=True, is_staff=True, **extra_fields
            )
            return user
        except:
            raise ValueError('An Error Occurred')



class CustomUser(AbstractUser):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length= 50)
    lastname = models.CharField(max_length= 50)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    objects = CustomUserManager()
    groups = models.ManyToManyField( 'auth.Group', related_name='custom_users', blank=True, help_text='The groups this user belongs to.', verbose_name='groups')
    user_permissions = models.ManyToManyField( 'auth.Permission', related_name='custom_users', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions', related_query_name='custom_user')
    

    def save(self, *args, **kwargs):
        self.username = f'{self.firstname} {self.lastname}'
        return super(CustomUser, self).save(*args, **kwargs)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
