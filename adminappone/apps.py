from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class customappconfig(AdminConfig):
    default_site = 'adminappone.admin.customadmin'

class AdminapponeConfig(AppConfig):
    name = 'adminappone'


