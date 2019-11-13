from __future__ import unicode_literals

from tkinter.ttk import Panedwindow, Labelframe, Separator

from mutagen.easyid3 import EasyID3
import youtube_dl
from tkinter import *
from tkinter import filedialog


class MyLogger(object):
    def debug(self, msg):
        print("DEBUG:", msg)

    def warning(self, msg):
        print("WARNING:", msg)

    def error(self, msg):
        print("ERROR:", msg)


def browse():
    destination.directory = filedialog.askdirectory()
    destination_directory.delete(0, last=END)
    destination_directory.insert(END, destination.directory)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def convert():
    global source_input
    global destination_directory
    global metadata_song_name_input
    global metadata_song_artist_input
    global metadata_song_album_input
    global metadata_song_releaseDate_input
    global metadata_song_genre_input
    global metadata_song_track_first_input
    global metadata_song_track_second_input

    url = source_input.get()
    directory = "{directory_here}/".format(directory_here=destination_directory.get())
    song_title = metadata_song_name_input.get()
    song_artist = metadata_song_artist_input.get()
    song_album = metadata_song_album_input.get()
    song_date = metadata_song_releaseDate_input.get()
    song_genre = metadata_song_genre_input.get()
    song_track = metadata_song_track_first_input.get()
    song_out_of = metadata_song_track_second_input.get()

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
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except youtube_dl.utils.DownloadError as e:
        print("An Error has occurred:", e, "\nPlease try again\n")
        return

    print("Adding metadata...")
    try:
        metatag = EasyID3(directory + song_title + '.mp3')
    except FileNotFoundError as e:
        print("An Error has occurred:", e, "\nPlease try again\n")
        return

    metatag['title'] = song_title
    print("DEBUG: Title successfully set")
    metatag['artist'] = song_artist
    print("DEBUG: Artist successfully set")
    metatag['date'] = song_date
    print("DEBUG: Published date successfully set")
    metatag['album'] = song_album
    print("DEBUG: Album successfully set")
    metatag['genre'] = song_genre
    print("DEBUG: Genre successfully set")
    metatag.RegisterTextKey("track", "TRCK")
    metatag['track'] = "{song_1}/{song_2}".format(song_1=song_track, song_2=song_out_of)
    print("DEBUG: Track successfully set")
    metatag.save()
    print("DEBUG: Metadata successfully saved")

    print("Complete!")


window = Tk()
window.title("Youtube Downloader")
window.geometry('560x500')

# Text
title = Label(window, text="Youtube Downloader", font=("Roboto", 20))
title.grid(column=0, row=0, columnspan=5)

title = Label(window, text="   ", font=("Roboto", 20))
title.grid(column=1, row=0)


p = Panedwindow(window, orient=VERTICAL)
p.grid(column=2, row=1, sticky="ew")

source = Labelframe(p, text='Source', width=500, height=200)
metadata = Labelframe(p, text='Metadata', width=500, height=200)
destination = Labelframe(p, text='Destination', width=500, height=200)
p.add(source)
p.add(metadata)
p.add(destination)

source_text = Label(source, text='Source:',)
source_text.grid(row=1, column=0, rowspan=2, pady=10, padx=5)
source_input = Entry(source, width=55)
source_input.grid(row=1, column=1, rowspan=2, padx=15)

metadata_subtitle = Label(metadata, text="(Leave blank for none)")
metadata_song_name_text = Label(metadata, text='Title:',)
metadata_song_artist_text = Label(metadata, text='Artist:',)
metadata_song_album_text = Label(metadata, text='Album:',)
metadata_song_releaseDate_text = Label(metadata, text='Released:',)
metadata_song_genre_text = Label(metadata, text='Genre:',)
metadata_song_track_text = Label(metadata, text='Track:',)
metadata_song_track_divider = Label(metadata, text='out of',)

metadata_subtitle.grid(row=0, column=0, padx=3, pady=3)
metadata_song_name_text.grid(row=1, column=0)
metadata_song_artist_text.grid(row=2, column=0)
metadata_song_album_text.grid(row=3, column=0)
metadata_song_releaseDate_text.grid(row=4, column=0)
metadata_song_genre_text.grid(row=5, column=0)
metadata_song_track_text.grid(row=6, column=0)
metadata_song_track_divider.grid(row=6, column=2)


metadata_song_name_input = Entry(metadata, width=45)
metadata_song_artist_input = Entry(metadata, width=45)
metadata_song_album_input = Entry(metadata, width=45)
metadata_song_releaseDate_input = Entry(metadata, width=45)
metadata_song_genre_input = Entry(metadata, width=45)
metadata_song_track_first_input = Entry(metadata, width=10)
metadata_song_track_second_input = Entry(metadata, width=10)

metadata_song_name_input.grid(row=1, column=1, columnspan=3)
metadata_song_artist_input.grid(row=2, column=1, columnspan=3)
metadata_song_album_input.grid(row=3, column=1, columnspan=3)
metadata_song_releaseDate_input.grid(row=4, column=1, columnspan=3)
metadata_song_genre_input.grid(row=5, column=1, columnspan=3)
metadata_song_track_first_input.grid(row=6, column=1)
metadata_song_track_second_input.grid(row=6, column=3)

destination_text = Label(destination, text="Destination file: ")
destination_text.grid(row=0, column=0)

destination_directory = Entry(destination, width=40)
destination_directory.grid(row=0, column=1)

destination_button = Button(destination, text="Browse", command=browse)
destination_button.grid(row=0, column=2, padx=10)


download_button = Button(window, text="Download", command=convert)
download_button.grid(column=2, row=2, sticky="ew", padx=20, pady=20)

window.mainloop()
