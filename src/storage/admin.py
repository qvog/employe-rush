from django.contrib import admin

from storage.models import (
    DefaultStorage,
    ReplyeStorage
)

admin.site.register(DefaultStorage)
admin.site.register(ReplyeStorage)