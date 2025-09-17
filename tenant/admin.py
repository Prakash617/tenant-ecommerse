# from django.contrib import admin

# # Register your models here.
# from .models import *


from django.contrib import admin
from .models import *
from django_tenants.admin import TenantAdminMixin

# Register your models here.
class DomainInline(admin.TabularInline):
    model= Domain
    max_num=1

@admin.register(Store)
class TenantAdmin(TenantAdminMixin,admin.ModelAdmin):
    list_display=(
        "store_name",
        "store_email",
        "store_visit_count",
        "active_theme",


    )
    inlines=[DomainInline]
admin.site.register(StoreCategory)
admin.site.register(StoreUnit)
