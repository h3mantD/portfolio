from django.contrib import admin

from .models import userdata, companyData, selected

# Register your models here.
admin.site.register(userdata)
admin.site.register(companyData)
admin.site.register(selected)