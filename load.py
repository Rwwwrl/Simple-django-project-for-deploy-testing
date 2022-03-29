from app import models


def create():
    author1 = models.Author(name='author_name_1')
    author2 = models.Author(name='author_name2')

    books_to_create = []
    for i in range(20):
        book = models.Book(
            title=f'book_title{i}',
            author=author1 if i % 2 else author2,
        )
        books_to_create.append(book)
    models.Author.objects.bulk_create((author1, author2))
    models.Book.objects.bulk_create(books_to_create)