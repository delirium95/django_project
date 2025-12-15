from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import LiteraryFormat, Book


class ModelTests(TestCase):
    def test_literary_format_str(self):
        literary_format = LiteraryFormat.objects.create(name="test")
        self.assertEqual(str(literary_format), literary_format.name)

    def test_author_str(self):
        author = get_user_model().objects.create(
            username="test",
            password="123123123",
            first_name="Alan",
            last_name="Doe"
        )
        self.assertEqual(str(author),
                         f"{author.username}: {author.first_name} {author.last_name}")

    def test_book_str(self):
        literary_format = LiteraryFormat.objects.create(name="test")
        book = Book.objects.create(title="Test", price=10.50, format=literary_format)
        self.assertEqual(str(book), f"{book.title} (price: {book.price}, format: {book.format.name})")

    def test_create_author_with_pseudonym(self):
        username = "Test"
        password = "123123"
        pseudonym = "Test Pseudonym"
        author = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name="John",
            last_name="Vasylkevych",
            pseudonym=pseudonym
        )
        self.assertEqual(author.username, username)
        self.assertTrue(author.check_password(password))
        self.assertEqual(author.pseudonym, pseudonym)
    