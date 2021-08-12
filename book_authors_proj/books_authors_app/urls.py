from django.urls import path     
from . import views


urlpatterns = [
    path('', views.home),
    path('books', views.indexBooks),
    path('authors', views.indexAuthors),
    path('add_books', views.addBooks),
    path('add_authors', views.addAuthors),
    path('books/<int:page_id>', views.books), 	   
    path('authors/<int:page_id>', views.authors),
    path('addBook2author/<int:author_id>', views.addBook2author), 
    path('addAuthor2book/<int:book_id>', views.addAuthor2book), 
    path('remove/<int:author_id>/<int:book_id>', views.remove),   
]