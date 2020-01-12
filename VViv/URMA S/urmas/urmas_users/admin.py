from django.contrib import admin
from .models import User

# Register my User model to my admin page
admin.site.register(User)