from django.contrib import admin
from .models import Contract, Payment, Category, Asset, Consumable, Staff

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class Category(admin.ModelAdmin):
    pass

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['name', 's_num', 'z_num']

@admin.register(Consumable)
class ConsumableAdmin(admin.ModelAdmin):
    pass

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass
