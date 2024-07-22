from django.contrib import admin


from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'created_at', 'likes_count')
    list_filter = ('created_at', 'user')
    search_fields = ('caption', 'user__username')
    inlines = [CommentInline]

    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = 'Likes'

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
# Register your models here.
