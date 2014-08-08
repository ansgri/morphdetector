
from PyQt4 import QtCore, QtGui
import sys

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(500, 300)
        self.setWindowTitle('Morph-Dete-Ctor')
        menubar = self.menuBar()
        loadImage = menubar.addMenu('&Load image')

        load = QtGui.QAction(QtGui.QIcon('png.png'), 'Open', self)
        load.setShortcut('Ctrl+O')
        load.setStatusTip('Open image for pattern')
        self.connect(load, QtCore.SIGNAL('triggered()'), self.getImg)

        loadImage.addAction(load)

        self.createDockWindows()

    def createDockWindows(self):
        dock = QtGui.QDockWidget("Group of points", self)

        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)

        widget = QtGui.QWidget()
        layout = QtGui.QGridLayout()

        blackLabel = QtGui.QLabel()
        blackLabel.setText("Black")
        layout.addWidget(blackLabel , 1, 1)

        blackListWidget = QtGui.QListWidget()
        blackListWidget.setFlow(0) #left to right
        for i in range(10):
            blackListWidget .addItem('( %s , %s )' % (i + 1, i + 2))
        layout.addWidget(blackListWidget , 1, 2)

        whiteLabel = QtGui.QLabel()
        whiteLabel.setText("White")
        layout.addWidget(whiteLabel, 2, 1)

        whiteListWidget = QtGui.QListWidget()
        whiteListWidget.setFlow(0) #left to right
        for i in range(10):
            whiteListWidget.addItem('( %s , %s )' % (i - 1, i - 2))
        layout.addWidget(whiteListWidget, 2, 2)

        widget.setLayout(layout)
        dock.setWidget(widget)


        #layout.addWidget(self.listWidget, 1)
        # dock.setWidget(self.listWidget)
        #dock.setWidget(layout)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)




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

# class FormWidget2(QtGui.QWidget):
#
#     def __init__(self, parent):
#         super(FormWidget2, self).__init__(parent)
#         self.layout = QtGui.QGridLayout(self)
#         self.layout.setSpacing(10)



app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())

