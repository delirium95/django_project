from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AuthorCreationForm
from .models import Book, Author, LiteraryFormat


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_visits": num_visits
    }
    return render(request, template_name="catalog/index.html", context=context)


class LiteraryFormatListView(LoginRequiredMixin, ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"
    queryset = LiteraryFormat.objects.all()


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    queryset = Book.objects.select_related("format")
    paginate_by = 10


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = "__all__"


def test_session_view(request: HttpRequest) -> HttpResponse:
    request.session["book"] = "Test session book"
    return HttpResponse(
        "<h1>Test Session</h1>"
    )


class LiteraryFormatCreateView(LoginRequiredMixin, CreateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-format-list")
    template_name = "catalog/literary-format-form.html"


class LiteraryFormatUpdateView(LoginRequiredMixin, UpdateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-format-list")
    template_name = "catalog/literary-format-form.html"


class LiteraryFormatDeleteView(LoginRequiredMixin, DeleteView):
    model = LiteraryFormat
    success_url = reverse_lazy("catalog:literary-format-list")
    template_name = "catalog/literary-format-confirm-delete.html"


class AuthorListView(LoginRequiredMixin, ListView):
    model = Author
    queryset = Author.objects.prefetch_related("books")
    paginate_by = 2


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorCreationForm


# def book_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
#     book = Book.objects.get(id=pk)
#     context = {
#         "book": book
#     }
#     return render(request, "catalog/book_detail.html", context=context)
