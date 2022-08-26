from django.contrib import admin
from app1.models import *
# Register your models here.
@admin.register(CreateStockGrp)
class stockgrpadmin(admin.ModelAdmin):
    list_display = ('id','name','alias','under','quantities')

@admin.register(CreateStockItem)
class stockitemadmin(admin.ModelAdmin):
    list_display = ('id','name','alias','under','unit','gst','supply','rduty','quantity','rate','per','value')

@admin.register(group_ananysis_view)
class group_ananysis_admin(admin.ModelAdmin):
    list_display = ('id','particular','iquantity','ieff_rate','ivalue','oquantity','oeff_rate','ovalue')

@admin.register(analysis_view)
class analysis_admin(admin.ModelAdmin):
    list_display = ('id','particular','iquantity','ieff_rate','ivalue','oquantity','oeff_rate','ovalue')

@admin.register(godown_model)
class godown_admin(admin.ModelAdmin):
    list_display = ('id','name','itm')

@admin.register(purchase_model)
class purchase_admin(admin.ModelAdmin):
    list_display = ('id','itm','name','qnt','brate','bvalue','addcost','totalvalue')

@admin.register(sale_model)
class sale_admin(admin.ModelAdmin):
    list_display = ('id','itm','name','qnt','brate','bvalue','addcost','totalvalue')

@admin.register(category_model)
class category_admin(admin.ModelAdmin):
    list_display = ('id','name','qnt','cost','saleprice')