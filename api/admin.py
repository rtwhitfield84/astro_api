from django.contrib import admin
from django.contrib.auth.models import User
from api.models import *

admin.site.register(User)
admin.site.register(tab_model.Tab)