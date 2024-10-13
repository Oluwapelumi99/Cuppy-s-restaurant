from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Customer, Table, Booking


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
