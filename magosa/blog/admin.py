from django.contrib import admin
from blog.models import contactFormModel
# Register your models here.


class contactFormModelAdmin(admin.ModelAdmin):
    list_display = ('username','message')

admin.site.register(contactFormModel,contactFormModelAdmin)