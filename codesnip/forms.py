from django import forms
from codesnip.models import Snippet
from codesnip.settings import SETTINGS
from pygments import highlight
from pygments import lexers
from pygments.formatters import HtmlFormatter


class SnippetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SnippetForm, self).__init__(*args, **kwargs)
        self.fields['language'].choices = sorted(self.fields['language']
                                                 .choices, key=lambda x: x[1])

    class Meta:
        exclude = ['pygmentized']
        model = Snippet

    def save(self, commit=True):
        snippet = super(SnippetForm, self).save(commit=False)
        language_lexer = getattr(lexers, snippet.language)
        formatter = HtmlFormatter(**SETTINGS['FORMATTER_ARGS'])
        snippet.pygmentized = highlight(snippet.code, language_lexer(),
                                        formatter)
        if commit:
            snippet.save()
        return snippet
