# myapp/admin.py

from django.contrib import admin
from .models import Profile,House

# Register the User model
admin.site.register(Profile)
# admin.site.register(House)

@admin.register(House)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'price', 'is_for_sale', 'date_posted')