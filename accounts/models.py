from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, 
										AbstractBaseUser, PermissionsMixin)

# Create your models here.

class CustomeUserManager(BaseUserManager):
	
	"""
	create model where email is 
	unique identifiers for 
	authentication.

	"""

	def create_user(self, username, email, password, **extra_fields):

		""" Create user and save email and password"""
		if not username:
			raise ValueError(_('The Username is missing'))
		if not email:
			raise ValueError(_('The Email must be set'))
		email = self.normalize_email(email)

		user = self.model(username=username, email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, username, email, password, **extra_fields):


		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError(_('SuperUser must be is_staff=True'))
		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_('SuperUser must be is is_superuser=True'))
		if extra_fields.get('is_active') is not True:
			raise ValueError(_('SuperUser must be is is_active=True'))

		return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(verbose_name='User Name',max_length=100, unique=True, null=True) 
	email = models.EmailField(
				verbose_name='email address',
				max_length=255,
				unique=True,
				)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = CustomeUserManager()

	def __str__(self):
		return self.username
