import sys
from logger.log import logger
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMainWindow, QGridLayout, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPalette, QImage, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from video_utils.video_utils import VideoThread
class camWidget(QWidget):
    def __init__(self, index, title, width, height):
        super().__init__()
        self.title = title
        self.width = width
        self.height = height
        self.index  = index
        self.resize(self.width, self.height)
        self.initUI()

    def initUI(self):
        self.setStyleSheet("border: 2px solid red;")

        self.label = QLabel(self)
        self.label.resize(self.width,self.height)
        if self.index is not None :
            th = VideoThread(self)
            th.changePixmap.connect(self.setImage)
            th.start()
            logger.debug('Thread launched for CAM {}'.format(self.index))
        

    @pyqtSlot(QImage)
    def setImage(self, image):
        video = QPixmap.fromImage(image)
        #video.resize(self.width, self.height)
        video = video.scaledToHeight(self.height)
        video = video.scaledToWidth(self.width)
        self.label.setPixmap(video)
        #self.label.setScaledContents(true)





class SMWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.initUI()


    def initUI(self):
        QToolTip.setFont(QFont('Sans-Serif', 10))

        self.setToolTip('This is a Cam Reccorder SoftWare')
        self.resize(self.width, self.height)
        self.setWindowTitle('Cam Reccorder Powered by Search_Map')
        self.setWindowIcon(QIcon('source_data/icon.png'))

        menu_bar = self.menuBar()
        config = menu_bar.addMenu('File')
        config = menu_bar.addMenu('Config')
        about = menu_bar.addMenu('About?')

        cam_1 = camWidget(0, "CAM 1", self.width/2, self.height/2)
        cam_2 = camWidget(None, "CAM 2", self.width/2, self.height/2)
        cam_3 = camWidget(None, "CAM 3", self.width/2, self.height/2)
        cam_4 = camWidget(None, "CAM 4", self.width/2, self.height/2)
        grid = QGridLayout()
        #grid.setSpacing(1)
        grid.addWidget(cam_1, 1, 1)
        grid.addWidget(cam_2, 1, 2)
        grid.addWidget(cam_3, 2, 1)
        grid.addWidget(cam_4, 2, 2)

        centralW = QWidget()
        centralW.resize(self.width, self.height)
        centralW.setLayout(grid)
        self.setCentralWidget(centralW)
        self.show()



def app(width, height):
    app = QApplication(sys.argv)
    w = SMWindow(width, height)
    sys.exit(app.exec_())
