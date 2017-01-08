from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .models import Leaderboard

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Leaderboard)
