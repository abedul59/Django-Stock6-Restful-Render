from django.contrib import admin

# Register your models here.
from images import models
from images.models import Images
from images.models import  Stock6Sign202212
admin.site.register(models.Images)
admin.site.register(models.Stock6Sign202212)