from pytube import YouTube, Playlist
the_playlist_url = "https://www.youtube.com/watch?v=dt240sVj0pY&list=PLFkwr6HjQax2KPy8Zhs7VTvFwJD8E2eka&index=4"
playlist = Playlist(the_playlist_url)
# playlist.download_all() #파이썬 파일과 같은 위치
# playlist.download_all('./video') #저장위치
print('The playlist has ' + str(len(playlist)) + ' urls')
counts = input('How many urls do you want to download? Input the number: ')
DOWNLOAD_MAX_LIST = int(counts)
if DOWNLOAD_MAX_LIST == 0:
    exit()

myList = []
for idx, url in enumerate(playlist):
    if idx >= DOWNLOAD_MAX_LIST:
        break
    yt = YouTube(url)
    vs = yt.streams.filter()
    # for i in range(len(vs)):
    #     print(i, '. ', vs[i])
    theVideo = vs.filter(progressive=True, type='video', file_extension='mp4').get_highest_resolution()
    # print(idx, theVideo)
    myDict = {
        'index': idx,
        'title' : theVideo.title,
        'type': theVideo.type,
        'subtype': theVideo.subtype,
        'filesize': theVideo.filesize,
        'stream': theVideo
    }
    myList.append(myDict)
    theAudio = vs.filter().get_audio_only()
    # print(idx, theAudio)
    myDict = {
        'index': idx,
        'title' : theAudio.title,
        'type': theAudio.type,
        'subtype': theAudio.subtype,
        'filesize': theAudio.filesize,
        'stream': theAudio
    }
    myList.append(myDict)

for idx, d in enumerate(myList):
    print(idx, d)

# videoNum = int(input("Which stream do you want to download? "))
# videoStreams[videoNum].download(DOWNLOAD_DIR)
# default_filename = videoStreams[videoNum].default_filename

