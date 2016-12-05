from django.contrib import admin

# Register your models here.
from .models import User
from .models import Leaderboard

admin.site.register(User);
admin.site.register(Leaderboard);
