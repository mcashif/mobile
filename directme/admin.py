from django.contrib import admin
from .models import DriverJob, Client, Driver

class DriverJobAdmin(admin.ModelAdmin):

    list_display = ('clientid','driverid','isdelivered')
    list_filter = ('clientid__name','driverid__name','isdelivered')
    search_fields = ['clientid__name']


class DriverAdmin(admin.ModelAdmin):

    list_display = ('id','name','phone')


class ClientAdmin(admin.ModelAdmin):

    list_display = ('id','name','phone')

admin.site.register(DriverJob,DriverJobAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Driver,DriverAdmin)
