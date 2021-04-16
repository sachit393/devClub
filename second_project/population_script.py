import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'second_project.settings')

import django
django.setup()
import random

from secondapp.models import Book
from faker import Faker

fakegen=Faker()
genre=['action','fiction','drama','motivation','acads']
def populate(N):
    for entry in range(N):
        fake_title=fakegen.name()
        fake_author=fakegen.name()
        fake_genre=random.choice(genre)
        fake_publisher=fakegen.company()
        fake_summary=fakegen.text()

        user=Book.objects.get_or_create(title=fake_title,author=fake_author,publisher=fake_publisher,genre=fake_genre,summary=fake_summary)[0]

if __name__ =='__main__':
    populate(20)
