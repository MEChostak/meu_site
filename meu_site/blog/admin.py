from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    list_filter = ('title', 'author', 'publish', 'status')
    raw_id_fields = ('author', )
    date_hierarchy = 'publish'
    search_fields = ('title', 'author', 'publish', 'status')
    prepopulated_fields = {'slug':('title',)}
