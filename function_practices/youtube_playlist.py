# Author : Kyungho Lim
# Contact : kyungho.lim@gmail.com

from pytube import YouTube, Playlist
import configparser
config = configparser.ConfigParser()
config.read('youtube_config.ini')
DOWNLOAD_DIR = config.get('download', 'download_dir')

the_playlist_url = input('Put your playlist url: ')
# the_playlist_url = "https://www.youtube.com/playlist?list=PLMhsC6kNtmg1qh9ujjfcujqxNRECPlLBp"

try:
    playlist = Playlist(the_playlist_url)
except:
    print('Wrong url. Program is closed. now')
    exit()

if not playlist:
    print('No streams in the playlist. Program is closed. now')
    exit(0)

print('The playlist has ' + str(len(playlist)) + ' streams')

counts = input('How many streams do you want to download? Input the number: ')
DOWNLOAD_MAX_LIST = int(counts)
if DOWNLOAD_MAX_LIST == 0 or DOWNLOAD_MAX_LIST > len(playlist):
    print('Your answer is not right. Program is closed now.')
    exit()

type = int(input('Choose the number of stream type in download (1.Video, 2.Audio): '))
print('Wait a moment...')

myList = []
for idx, url in enumerate(playlist):
    if idx >= DOWNLOAD_MAX_LIST:
        break
    yt = YouTube(url)
    vs = yt.streams.filter()
    # for i in range(len(vs)):
    #     print(i, '. ', vs[i])
    if type == 1:
        theVideo = vs.filter(progressive=True, type='video', file_extension='mp4').get_highest_resolution()
        # print(idx, theVideo)
        myDict = {
            'index': idx,
            'title' : theVideo.title,
            'type': theVideo.type,
            'subtype': theVideo.subtype,
            'filename': theVideo.default_filename,
            'filesize': theVideo.filesize,
            'stream': theVideo
        }
        myList.append(myDict)

    if type == 2:
        theAudio = vs.filter().get_audio_only()
        # print(idx, theAudio)
        myDict = {
            'index': idx,
            'title' : theAudio.title,
            'type': theAudio.type,
            'subtype': theAudio.subtype,
            'filename': theAudio.default_filename,
            'filesize': theAudio.filesize,
            'stream': theAudio
        }
        myList.append(myDict)

print('The downloadable streams are as follows:\n')
totalsize = 0
for idx, dict in enumerate(myList):
    totalsize += float(dict.get('filesize'))
    print(idx, dict)

print('\nThe total size is', '{:,}'.format(totalsize/1000000) + 'MB')
answer = input('Shall I download the streams above? (y/n): ')
if answer == 'n':
    print('Download cancelled. Program is closed now.')
    exit()

if answer == 'y':
    for idx, dict in enumerate(myList):
        theStream = dict.get('stream')
        title = dict.get('title')
        filesize = float(dict.get('filesize'))
        filename = dict.get('filename')
        print(' Downloading #' + str(idx) + '. [Size]', '{:,}'.format(filesize), 'bytes [file] ' + filename)
        theStream.download(DOWNLOAD_DIR)
