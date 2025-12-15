from django.urls import path

from catalog.views import (index,
                           LiteraryFormatListView,
                           BookListView,
                           BookDetailView,
                           test_session_view,
                           LiteraryFormatCreateView,
                           LiteraryFormatUpdateView,
                           LiteraryFormatDeleteView,
                           AuthorCreateView,
                           AuthorListView,
                           AuthorDetailView,
                           BookCreateView)

app_name = "catalog"

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("literary-formats/create/", LiteraryFormatCreateView.as_view(), name="literary-format-create"),
    path("literary-formats/<int:pk>/update/", LiteraryFormatUpdateView.as_view(), name="literary-format-update"),
    path("literary-formats/<int:pk>/delete/", LiteraryFormatDeleteView.as_view(), name="literary-format-delete"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/create", BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/create/", AuthorCreateView.as_view(), name="author-create"),
    path("test-session/", test_session_view, name="test-session")
]

