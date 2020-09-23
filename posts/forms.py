from django import forms
from posts.models import Author


class PostForm(forms.Form):
    title = forms.CharField(label='Tytuł', required=False)
    content = forms.CharField(label='Treść', widget=forms.Textarea, required=False)
    author_id = forms.ModelChoiceField(label='Wybierz autora', queryset=Author.objects.all(), initial=1, required=False)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        author = cleaned_data.get('author_id')

        if not (title and content):
            raise forms.ValidationError("Musisz uzupełnić wszystkie wartości!")
        elif author is None:
            raise forms.ValidationError("Musisz uzupełnić wszystkie wartości!")


class AuthorForm(forms.Form):
    nick = forms.CharField(label='Nick', required=False)
    email = forms.EmailField(label='E-mail', required=False)
    bio = forms.CharField(label='Krótkie bio', widget=forms.Textarea, required=False)

    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        email = cleaned_data.get('email')

        if not (nick and email):
            raise forms.ValidationError("Musisz uzupełnić nick oraz email!")
