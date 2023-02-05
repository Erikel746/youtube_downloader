import sys
from pytube import YouTube
import os
user = ""
while user != "n":
    link = input("Youtube Link: ")
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    yd = yt.streams.get_highest_resolution()
    desktop = os.path.expanduser("~/Desktop")
    yd.download(desktop)

    print("Video wurde auf dem Desktop heruntergeladen")

    user = input("Soll noch ein Video heruntergeladen werden? y/n\n")

