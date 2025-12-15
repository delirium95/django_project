from django.contrib.auth.forms import UserCreationForm

from catalog.models import Author


class AuthorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Author
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name","pseudonym", )