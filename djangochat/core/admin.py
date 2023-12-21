from django.contrib import admin

# Register your models here.
from .models import CustomUser  # Import your custom user model

admin.site.register(CustomUser)