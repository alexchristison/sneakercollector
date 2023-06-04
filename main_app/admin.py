from django.contrib import admin
from .models import Sneaker, Worn, Sock
# Register your models here.
admin.site.register(Sneaker)
admin.site.register(Worn)
admin.site.register(Sock)