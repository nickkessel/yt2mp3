from pytube import YouTube
from pytube import Playlist

import os
import moviepy.editor as mp
import re
import pyfiglet

welcome = pyfiglet.figlet_format("yt 2 mp3", font = "slant")
print(welcome)
print("\n yt2mp3 is a simple python application that uses pytube and moviepy to download audio from a given YouTube playlist link, and convert into an mp3 file.")

ytlink = input("Please paste the link to the youtube playlist you want to download music from: ")
playlist = Playlist(ytlink)
#pritn vid url
playlist.video_urls

for url in playlist:
    print(url)

#pritn address of yt object in playlist

for vid in playlist.videos:
    print(vid)

for url in playlist:
    YouTube(url).streams.filter(only_audio=True).first().download('/Users/nickk/Desktop/music')

folder = "/Users/nickk/Desktop/music"

for file in os.listdir(folder):
    if re.search('mp4', file):
        mp4_path = os.path.join(folder,file)
        mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
