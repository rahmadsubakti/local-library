from django.db import models
from django.urls import reverse

"""
Do not migrate it until approved"""
# Create your models here.
class Language(models.Model):
    """
    Object for language of book
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('language', kwargs={'slug':self.slug})

class Genre(models.Model):
    """
    Genre for books. A book is able to have one or more genres
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre', kwargs={'slug':self.slug})

class Author(models.Model):
    """
    Authors of book
    """
    name = models.CharField(max_length=200) # it's full name
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author", kwargs={"slug": self.slug})

class Book(models.Model):
    """
    Model representing data about book in catalog
    """
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=200)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre, help_text='Select one or many genres')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True,related_name='book_datas')
    description = models.TextField() # description of book
    cover = models.ImageField(upload_to='media/cover', blank=True, null=True) # Cover of book
    isbn = models.CharField('ISBN', max_length=13)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book", kwargs={"slug": self.slug})

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all())

    def display_author(self):
        return ', '.join(author.name for author in self.author.all())

    def quantity_all(self):
        """
        Quantity of all physical books
        """
        return len(self.books.all())

    def quantity_available(self):
        """
        Quantity of all physical books that are on loan.
        """
        return len(self.books.filter(status='a'))

class BookInstance(models.Model):
    """
    Model representing physical books in library
    """
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
    )
    id = models.CharField(max_length=10, primary_key=True, help_text="A spesific id of physical book")
    book = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE)
    status = models.CharField('Loan Status', max_length=1, choices=LOAN_STATUS, default='m', help_text='Loan status of physical book')
    due_back = models.DateField(null=True, blank=True) # Due back of physical book

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return '{id} - {title}'.format(id=self.id, title=self.book.title)