import os
import subprocess
from pytube import YouTube, Playlist
import configparser
config = configparser.ConfigParser()
config.read('youtube_config.ini')
DOWNLOAD_DIR = config.get('download', 'downlaod_dir')

yt = YouTube("https://www.youtube.com/watch?v=VMXTeEkAxeo")
videoStreams = yt.streams.filter()
for i in range(len(videoStreams)):
    print(i, '. ', videoStreams[i])
# print(videoStreams)
theVideo = videoStreams.filter(progressive=True, type='video', file_extension='mp4').get_highest_resolution()
print(theVideo)
theAudio = videoStreams.filter().get_audio_only()
print(theAudio)
# videoStreams = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
# print(videoStreams)
# print(videoStreams.url)
# print(videoStreams.default_filename)
# print(videoStreams.title)
# print(videoStreams.type)
# print(videoStreams.subtype)
# print(videoStreams.video_codec)
# print(videoStreams.filesize)
# videoStreams = yt.streams.filter(progressive=True, file_extension='mp4')
# for i in range(len(videoStreams)):
#     print(i, '. ', videoStreams[i])
# videoNum = int(input("Which stream do you want to download? "))
# videoStreams[videoNum].download(DOWNLOAD_DIR)
# default_filename = videoStreams[videoNum].default_filename
