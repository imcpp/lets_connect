from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
admin.site.register(User,UserAdmin)

admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Comment)
admin.site.register(Post)
