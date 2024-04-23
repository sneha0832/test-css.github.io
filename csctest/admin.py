from django.contrib import admin
from .models import Exhibit
from .models import Activity
from .models import TypeofPlay

admin.site.register(TypeofPlay)
admin.site.register(Activity)
@admin.register(Exhibit)
class HTMLPageAdmin(admin.ModelAdmin):
    list_display = ('title',)

class TypePlayAdmin(admin.ModelAdmin):
    list_display = ('TypeName', 'Description')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['ActivityID', 'Name', 'Category', 'Subcategory', 'Description']
