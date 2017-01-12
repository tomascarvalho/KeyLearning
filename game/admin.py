from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .models import Leaderboard, Scenarios, Scenario_Completed_By

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Leaderboard)
admin.site.register(Scenarios)
admin.site.register(Scenario_Completed_By)
