from django.shortcuts import redirect, render, HttpResponse
from .models import *

def home(request):
    return render(request, 'home.html')

def indexBooks(request):
    data = {
        'books' : Book.objects.all()
    }
    return render(request, 'addBooks.html', data)

def addBooks(request):
    bookTitle = request.POST['title']
    bookDesc = request.POST['desc']
    Book.objects.create(title = bookTitle, desc = bookDesc)
    return redirect(request.META.get('HTTP_REFERER'))

def addAuthors(request):
    authorFirstName = request.POST['first-name']
    authorLastName = request.POST['last-name']
    authorNotes = request.POST['notes']
    Author.objects.create(first_name = authorFirstName, last_name = authorLastName, notes = authorNotes)
    return redirect(request.META.get('HTTP_REFERER'))

def indexAuthors(request):
    data = {
        'authors' : Author.objects.all()
    }
    return render(request, 'addAuthors.html', data)

def books(request, page_id):
    book = Book.objects.get(id=page_id)
    authors = book.authors.all()
    inHere = [author.id for author in book.authors.all()]
    print('In here:', inHere)
    notHere = [author for author in Author.objects.all() if author.id not in inHere]
    print('Not in here:', notHere)
    data = {
        'book' : book,
        'authors' : authors,
        'notHere' : notHere
    }
    return render (request, 'books.html', data)

def authors(request, page_id):
    author = Author.objects.get(id=page_id)
    books = author.books.all()
    bInHere = [book.id for book in author.books.all()]
    print('In here:', bInHere)
    bNotHere = [book for book in Book.objects.all() if book.id not in bInHere]
    print('Not in here:', bNotHere)
    data = {
        'author' : author,
        'books' : books,
        'bNotHere' : bNotHere
    }
    return render(request, 'authors.html', data)


def addBook2author(request, author_id):
    author = Author.objects.get(id=int(author_id))
    idBook= int(request.POST['book-id'])
    book = Book.objects.get(id=idBook)
    book.authors.add(author)
    return redirect(request.META.get('HTTP_REFERER'))

def addAuthor2book(request, book_id):
    book = Book.objects.get(id=int(book_id))
    idAuthor = int(request.POST['author-id'])
    author = Author.objects.get(id=idAuthor)
    author.books.add(book)
    return redirect(request.META.get('HTTP_REFERER'))


def remove(request, author_id, book_id):
    author = Author.objects.get(id=int(author_id))
    book = Book.objects.get(id=int(book_id))
    # book_id = int(request.POST['book-id'])
    # book = Book.objects.get(id=book_id)
    # print(book)
    #author.books.remove(book)
    return redirect(request.META.get('HTTP_REFERER'))
