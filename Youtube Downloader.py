from __future__ import unicode_literals
from mutagen.easyid3 import EasyID3
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        print("DEBUG:", msg)

    def warning(self, msg):
        print("WARNING:", msg)

    def error(self, msg):
        print("ERROR:", msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def convert(directory, song_title, url, song_artist, song_date, song_album, song_genre, song_track, song_out_of):
    print("Downloading...")
    outtmpl = directory + song_title + '.%(ext)s'

    ydl_opts = {
        'outtmpl': outtmpl,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Adding metadata...")
    metatag = EasyID3(directory + song_title + '.mp3')
    metatag['title'] = song_title
    metatag['artist'] = song_artist
    metatag['date'] = song_date
    metatag['album'] = song_album
    metatag['genre'] = song_genre
    metatag.RegisterTextKey("track", "TRCK")
    metatag['track'] = "{song_1}/{song_2}".format(song_1=song_track, song_2=song_out_of)
    metatag.save()

    print("Complete!")


print("Open Source Youtube to MP3 converter")
print("Source code found here: https://github.com/daniel071/Youtube_Downloader")
print("Created by Daniel Pavela")
print("\n --------------------- \n")

while True:
    user_URL = input("Input Youtube URL: ")
    user_directory = input("Input output folder: ")
    user_title = input("Input Song Title: ")
    user_artist = input("Input Song Artist: ")
    user_release = input("Input Song Release Date: ")
    user_album = input("Input Song Album: ")
    user_genre = input("Input Song Genre: ")
    user_currentTrack = input("Input Song Current Track: ")
    user_allTracks = input("Input Song Amount of tracks: ")

    convert(user_directory, user_title, user_URL, user_artist, user_release, user_album, user_genre, user_currentTrack, user_allTracks)

    input("\nPress any key to continue...")
