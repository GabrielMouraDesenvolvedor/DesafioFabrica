import requests
from django.core.management.base import BaseCommand
from authors.models import Joke

class Command(BaseCommand):
    help = 'Fetch a random Chuck Norris joke'

    def handle(self, *args, **kwargs):
        response = requests.get('https://api.chucknorris.io/jokes/random')
        if response.status_code == 200:
            joke_text = response.json().get('value')
            Joke.objects.create(joke_text=joke_text)
            self.stdout.write(self.style.SUCCESS('Joke saved successfully'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch joke'))
