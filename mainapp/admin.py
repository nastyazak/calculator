from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Category)
admin.site.register(TypeWork)
admin.site.register(Order)
admin.site.register(OrderWork)
