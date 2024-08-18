from django.views.generic.detail import DetailView
from .views import list_books, LibraryDetailView


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
