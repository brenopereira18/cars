from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') #informa os campos que quer mostrar na pagina de admin
    search_fields = ('model',) #permite buscar por dados através do model, neste caso


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin) 
#pede como parâmetro o modelo(tabela) e o que vai ser passado para a tabela na pagina admin