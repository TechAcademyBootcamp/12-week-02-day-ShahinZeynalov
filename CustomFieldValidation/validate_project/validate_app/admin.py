from django.contrib import admin
from .models import CustomModel,State
# Register your models here.

admin.site.register([CustomModel,State])
