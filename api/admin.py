from django.contrib import admin
from .models import Task, phoneModel, User

# Register your models here.
admin.site.register(Task)

admin.site.register(phoneModel)

admin.site.register(User)