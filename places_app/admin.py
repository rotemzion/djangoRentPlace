from django.contrib import admin
from django.db import models
from .models import ItemLocation, UserP,Renters

admin.site.register(ItemLocation)
admin.site.register(UserP)
admin.site.register(Renters)
