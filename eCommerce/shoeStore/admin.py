from django.contrib import admin
from .models import *
# Register your models here.
class NewsLetterAdmin(admin.ModelAdmin):
    list_display=("email",)
class ShoeAdmin(admin.ModelAdmin):
    list_display=("name","price")
class PaymentInfoAdmin(admin.ModelAdmin):
    list_display=("first_name","card_number")
admin.site.register(Shoe,ShoeAdmin)
admin.site.register(PaymentInfo,PaymentInfoAdmin)
admin.site.register(NewsLetter,NewsLetterAdmin)

