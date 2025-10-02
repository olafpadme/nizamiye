from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin     
from datetime import datetime 
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)            
from .models import UserData

# @admin.register(UserData)
# class UserDataAdmin(admin.ModelAdmin):
#     list_display = ("tckn", "ziyaret", "user", "giris", "cikis")
#     list_filter = ("ziyaret", "giris", "cikis")
#     search_fields = ("tckn", "aciklama")


class UserDataResources(resources.ModelResource):

    class Meta:
        model = UserData



@admin.register(UserData)
class BookAdmin(ImportExportModelAdmin):
    resource_classes = [UserDataResources]
    list_display = ("tckn", "ziyaret", "user", "giris", "cikis")
    list_filter = ("ziyaret", # "giris", "cikis",
                   ("giris", DateRangeFilterBuilder()),
                   ('cikis', DateRangeFilterBuilder()),
        )
    search_fields = ("tckn", "aciklama")
