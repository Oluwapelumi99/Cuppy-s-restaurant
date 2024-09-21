from django.contrib import admin
from .models import Customer, Table, Booking
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):

    list_display = ('title', 'forename', 'surname')
    search_fields = ['title']
    summernote_fields = ('content',)

@admin.register(Table)
class TableAdmin(SummernoteModelAdmin):

    list_filter = ('seats',)

# Register your models here.
admin.site.register(Booking)


