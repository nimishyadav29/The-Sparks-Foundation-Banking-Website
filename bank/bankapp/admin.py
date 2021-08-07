from django.contrib import admin

# Register your models here.
from .models import customer,transfer_history
admin.site.register(customer)
admin.site.register(transfer_history)