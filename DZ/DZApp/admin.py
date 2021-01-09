from django.contrib import admin
from .models import Partner, Provider, Partnership, Product, Waybill, Tables, TestProvider

admin.site.register(Partner)
admin.site.register(Provider)
admin.site.register(Partnership)
admin.site.register(Product)
admin.site.register(Waybill)
admin.site.register(Tables)
admin.site.register(TestProvider)