from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language


class BooksInline(admin.StackedInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    # Cannot add ManyToManyField genre here
    fields = [('title', 'author'), 'slug', 'summary',
              ('isbn', 'language'), 'genre', ]
    list_display = ('title', 'author', 'language', display_genre)

    # inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('id', 'book', 'imprint')
        }),
        ('Availability', {
            'fields': [('status', 'due_back')]
        }),
    )


admin.site.register(Genre)

admin.site.register(Language)
