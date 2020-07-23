from django.contrib import admin
from .models import Bible, NA27Bible, LXXBible, VULBible


admin.site.register(Bible)
admin.site.register(NA27Bible)
admin.site.register(LXXBible)
admin.site.register(VULBible)
