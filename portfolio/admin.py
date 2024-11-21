from django.contrib import admin
from .models import MyProject, GuestBook, Blog

admin.site.register(MyProject)
admin.site.register(GuestBook)
admin.site.register(Blog)
# admin.site.register(Service)
