__author__ = 'MillerB'

import csv
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "noraebook.settings")
django.setup()
from webapp.models import Song, Company


class SongImporter:

    def __init__(self, song_model, company_model):
        self.song_model = song_model
        self.company_model = company_model

    @staticmethod
    def tuples_from_csv(file_path):
        open_file = open(file_path, encoding="utf8")
        new_list = []
        for row in csv.reader(open_file):
            new_tuple = [str(row[i]).strip() for i in range(len(row))]
            new_list.append(new_tuple)
        return new_list

    def song_already_in_db(self, code, company_name):
        company = self.company_model.objects.filter(name=company_name)
        song_already_in_db = len(self.song_model.objects.filter(code=code, company=company)) > 0
        return song_already_in_db

    def import_from_file(self, file_path, company_name):
        tuples = self.tuples_from_csv(file_path)
        for t in tuples:
            code = int(t[0])
            if self.song_already_in_db(code, company_name) is False:
                title = str(t[1]).encode('utf8')
                artist = str(t[2]).encode('utf8')
                company = self.company_model.objects.filter(name=company_name)[0]
                new_song = self.song_model(code=code, title=title, artist=artist, company=company)
                new_song.save()
                #log = 'Success!: %s: "%s" by %s added to the database.' % (code, title, artist)
            else:
                log = 'Song not added: Song code %s is already in the database for %s.' % (code, company_name)
                print(log)
        return


if __name__ == "__main__":
    importer = SongImporter(Song, Company)
    importer.import_from_file("scripts/csv/song_list.csv", "TJ Media")
