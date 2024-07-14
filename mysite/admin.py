from django.contrib import admin
from polls.models import Choice, Question



class CustomerAdminSite(admin.AdminSite):
    site_header = "Curso de python Admin"


admin_site = CustomerAdminSite()
# admin_site.register(MyModel)
admin_site.register(Choice)
admin_site.register(Question)