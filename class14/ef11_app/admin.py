from django.contrib import admin
# from .models import Banner,Category, Product
from .models import *
# Register your models here.

admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Contact)
