

# Register your models here.
from django.contrib import admin
from .models import HelpRequest

admin.site.register(HelpRequest)



class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'help_type', 'area', 'is_accepted', 'accepted_by', 'created_at')
    list_filter = ('is_accepted', 'area')
    search_fields = ('help_type', 'description', 'area')
