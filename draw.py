from PyQt4 import QtCore, QtGui
import sys

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        #self.resize(250, 150)
        self.setWindowTitle('Morph-Dete-Ctor')
        menubar = self.menuBar()
        loadImage = menubar.addMenu('&Load image')

        load = QtGui.QAction(QtGui.QIcon('icon.png'), 'Open', self)
        load.setShortcut('Ctrl+O')
        load.setStatusTip('Open image for pattern')
        self.connect(load, QtCore.SIGNAL('triggered()'), self.getImg)

        loadImage.addAction(load)


    def getImg(self):
        imgName = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 'C:/')
        self.formWidget = FormWidget(self, imgName)
        self.setCentralWidget(self.formWidget)


class FormWidget(QtGui.QWidget):
    def __init__(self, parent, imgPath):
        super(FormWidget, self).__init__(parent)
        self.label = QtGui.QLabel()
        img = QtGui.QPixmap(imgPath)
        scaledImg = img.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)# to view pictures
        self.label.setPixmap(scaledImg)

        self.label.setScaledContents(True)#changes size of window



        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(self.label)









app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())

