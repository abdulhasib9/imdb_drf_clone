from django.contrib import admin
from . import models

admin.site.register(models.Watchlist)
admin.site.register(models.StreamPlatform)
admin.site.register(models.Review)