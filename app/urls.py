from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('get_books/', cache_page(5 * 60)(views.GetBooksView.as_view()), name='get_books'),
]
