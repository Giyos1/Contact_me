from django.contrib import admin
from .models import Contact, PhoneNumber


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    pass
