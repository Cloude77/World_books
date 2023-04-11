from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance
from django.views import generic


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.all().count()
    #filter(status_exact=4)
    num_authors = Author.objects.count()
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_available': num_instances_available,
                           'num_authors': num_authors, })


class BookListView(generic.ListView):
    model = Book



