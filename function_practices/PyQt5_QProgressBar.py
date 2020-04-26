import sys
import os
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QLabel, QVBoxLayout
from PyQt5.QtCore import QBasicTimer
from pytube import YouTube, Playlist

import configparser
config = configparser.ConfigParser()
config.read('youtube_config.ini')
DOWNLOAD_DIR = config.get('download', 'downlaod_dir')

DOWNLOAD_MAX_LIST = 1

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        winLayout = QVBoxLayout()
        self.btnList = QPushButton('리스트 가져오기', self)
        self.lblList = QLabel('준비중')
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btnList.clicked.connect(self.getList)
        self.btn.clicked.connect(self.doAction)

        winLayout.addWidget(self.btnList)
        winLayout.addWidget(self.lblList)
        winLayout.addWidget(self.pbar)
        winLayout.addWidget(self.btn)
        self.setLayout(winLayout)

        self.timer = QBasicTimer()
        self.step = 0
        self.currentSize = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


    def getList(self):
        self.youtube_download()
        if self.theStream:
            self.lblList.setText('리스트준비완료')

    def timerEvent(self, e):
        if self.theStream:
            self.theStream.download(DOWNLOAD_DIR)
        # while self.currentSize <= self.filesize:
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        # time.sleep(1)
        try:
            self.currentSize = os.path.getsize(DOWNLOAD_DIR + '/' + self.filename)
        except:
            self.currentSize = 0
        self.step = self.currentSize / self.filesize * 100
        print(str(self.currentSize), str(self.filesize), str(self.step) + '%')
        self.pbar.setValue(self.step)
        # return

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


    def youtube_download(self):
        the_playlist_url = "https://www.youtube.com/watch?v=dt240sVj0pY&list=PLFkwr6HjQax2KPy8Zhs7VTvFwJD8E2eka&index=4"
        playlist = Playlist(the_playlist_url)
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
                'filename' : theVideo.default_filename,
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
                'filename': theAudio.default_filename,
                'filesize': theAudio.filesize,
                'stream': theAudio
            }
            myList.append(myDict)

        self.theStream = myList[0].get('stream')
        self.filesize = myList[0].get('filesize')
        self.filename = myList[0].get('filename')
        # for idx, d in enumerate(myList):
        #     print(idx, d)
        #     theStream = d[0].get('stream')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())