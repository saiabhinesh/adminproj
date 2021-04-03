from django.contrib import admin
from .models import *

class customadmin(admin.AdminSite): #defualt admin overiding apps,settings change
    site_header = "my site header"
    site_title = "my site title"
    index_title = 'my index title'

class adminone(admin.AdminSite): #another admin
    site_header='admin one site header'

class padmin(admin.ModelAdmin):
    print("in model")
    fields = ['pname']

adm1=adminone(name='admone')
adm1.register(person,padmin)

refcustomadmin=customadmin(name='admcsu')
from django.apps import apps
models = apps.get_models()
for model in models:
    refcustomadmin.register(model)
#refcustomadmin.site.unregister(django.contrib.sessions.models.session) need to change syntax