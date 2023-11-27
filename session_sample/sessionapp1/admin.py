from django.contrib import admin
from . models import movies,Director,CensorInfo,Actor

# Register your models here.

admin.site.register(movies)
admin.site.register(Director)
admin.site.register(CensorInfo)
admin.site.register(Actor)

