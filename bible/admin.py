from django.contrib import admin
from .models import Bible
from import_export import resources


admin.site.register(Bible)

class BiResource(resources.ModelResource):

    class Meta:
        model = Bible
