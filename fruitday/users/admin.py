from django.contrib import admin
from models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "password", "email", "addressee",
                    "address", "zip_code", "cellphone"]

admin.site.register(UserInfo,UserInfoAdmin)
