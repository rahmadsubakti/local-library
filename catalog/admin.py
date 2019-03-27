from django.contrib import admin

from catalog.models import Language, Genre, Author, Book, BookInstance
# Register your models here.
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'display_genre', 'quantity_all', 'quantity_available')
    list_filter = ('genre', 'author', 'language')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status',)
    list_filter = ('status',)
    search_fields = ['id']