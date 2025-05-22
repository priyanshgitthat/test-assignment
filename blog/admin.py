from django.contrib import admin
from .models import Category, BlogPost

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Keep other configurations
    # Remove the prepopulated_fields line completely

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'status', 'truncated_summary')
    list_filter = ('category', 'status', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('truncated_summary',)  # Shows the truncated summary in admin

admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)