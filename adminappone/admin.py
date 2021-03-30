from django.contrib import admin

# Register your models here.
class customadmin(admin.AdminSite):
    site_header = "my site header"
    site_title = "my site title"
    index_title = 'my index title'

csad=customadmin()#if models are there register here