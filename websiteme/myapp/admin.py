# myapp/admin.py

from django.contrib import admin
from .models import Profile,House

# Register the User model
admin.site.register(Profile)
admin.site.register(House)