from django.contrib import admin
from .models import UserData

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ("tckn", "ziyaret", "user", "giris", "cikis")
    list_filter = ("ziyaret", "giris", "cikis")
    search_fields = ("tckn", "aciklama")
