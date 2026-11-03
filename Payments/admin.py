from django.contrib import admin
from .models import Products
# Register your models here.
admin.site.register(Products)
admin.site.site_header = "Mpesa Admin"
admin.site.site_title = "Mpesa Admin Portal"
admin.site.index_title = "Welcome to Mpesa Admin Portal"
