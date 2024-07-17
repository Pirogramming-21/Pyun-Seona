from django.contrib import admin
from .models import Post, DevTool
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'devtool', 'interest')
    search_fields = ('title', 'content')
    list_filter = ('devtool', 'interest')
    
class DevToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'kind', 'content']
    search_fields = ['name', 'kind']

admin.site.register(Post, PostAdmin)
admin.site.register(DevTool, DevToolAdmin)