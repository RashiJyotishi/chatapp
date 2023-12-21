# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth.models import Group, Permission

# Add related_name to avoid clashes

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150 , unique=True , default="", null=False, blank=False)
    password = models.CharField(max_length=128 , default="", null=False, blank=False)
    # add any custom fields here

    
    class Meta:
        default_permissions = ()
        permissions = ()

      # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core.CustomUser.groups+',  # Change this related_name as needed
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='auth.User.user_permissions+',  # Change this related_name as needed
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


    def __str__(self):
        return self.username
        # return self.password
    