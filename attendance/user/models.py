from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.db import models

from django.utils import timezone

from django.utils.translation import gettext_lazy as _




from .managers import CustomUserManager

import uuid





#The user entity in the system.

#Users in the system are basically 3 types:

# 1)University Admin

# 2)Agents affiliated to the university




#Assuming mode of verification to be email (We will use sendgrid for that)

#Authentication will be provided as JWT(JSON Web token)





class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)

    phone = models.CharField(unique=True,max_length=20)

    address = models.TextField()

    password = models.TextField()

    country = models.CharField(max_length=30)

    uuid = models.UUIDField(default=uuid.uuid4,editable = False)

    




    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now,editable=False)

    verified = models.BooleanField(default=False)




    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []




    objects = CustomUserManager() #objects are mapped to this manager.

    def __str__(self):

        return self.email