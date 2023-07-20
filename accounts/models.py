from django.core.mail import send_mail
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
import uuid

import blog


class UserManager(BaseUserManager):
    def create_user(self,email,password=None,is_active=False,is_staff=False,is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,

        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin = True,

        )


        return user



class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_email_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


