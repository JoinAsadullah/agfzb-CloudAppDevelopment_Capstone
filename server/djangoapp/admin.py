from django.contrib import admin
from .models import CarMake, CarModel


# Define an inline model for CarModel
class CarModelInline(admin.TabularInline):
    model = CarModel

# Register CarMake model and include the inline CarModel model
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
