from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Joke(models.Model):
    joke_text = models.TextField()

    def __str__(self):
        return self.joke_text[:50]  # Mostra os primeiros 50 caracteres
