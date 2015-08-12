__author__ = 'MillerB'


import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "noraebook.settings")
django.setup()

print("this")


from search.models import Song, Company
print(len(Song.objects.order_by('artist')[:]))

