
from django.contrib import admin
from base.models import Profile
from django.contrib.auth import get_user_model

"""Register Profile Model to Admin Panel"""
admin.site.register(get_user_model())

admin.site.register(Profile)
