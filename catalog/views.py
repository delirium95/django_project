from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AuthorCreationForm, BookForm, BookSearchForm
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
    paginate_by = 5

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(BookListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = BookSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        queryset = Book.objects.select_related("format")
        form = BookSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm


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
