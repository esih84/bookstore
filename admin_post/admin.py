from django.contrib import admin
from .models import Books , Category
# Register your models here.

class categoryadmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category,categoryadmin)

class adminpost(admin.ModelAdmin):
    list_display = ('bookName', 'slug', 'publish', 'description')
    search_fields = ('description', 'bookName')
    list_filter = ('publish', 'status')
    prepopulated_fields = {'slug': ('bookName',)}
    ordering = ['status', 'publish']

admin.site.register(Books,adminpost)