from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_filter = ["title", "author", "publication_year"]
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')


# Register your models here.
admin.site.register(Book)