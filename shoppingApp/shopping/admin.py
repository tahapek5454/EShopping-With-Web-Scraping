from django.contrib import admin
from .models import Products
# Register your models here.
# admin uygulamasında gostertiyoruz


class ProductAdmin(admin.ModelAdmin):

    # neler gosterilecek
    list_display = ("marka", "modelAdi", "modelNo", "prodTitle", "fiyat", "site")

    search_fields = ("marka", "modelNo", "modelAdi", "site")

# gosterecegiz
admin.site.register(Products, ProductAdmin)
