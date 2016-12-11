from django.db import models
from pygments.lexers import LEXERS


class Snippet(models.Model):
    LANGUAGE_CHOICES = [(lexer, LEXERS[lexer][1]) for lexer in LEXERS]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    language = models.CharField(max_length=255, choices=LANGUAGE_CHOICES)
    code = models.TextField()
    pygmentized = models.TextField(blank=True)

    def __str__(self):
        return '%s' % self.slug
