from django.contrib import admin
from .models import New

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_of_creation',)
    ordering = ('status',) #mortb sazi br asas f{{ }}



admin.site.register(New, PostAdmin)

