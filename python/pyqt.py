import sys,random
from PyQt4 import QtGui,QtCore


class QuitButton(QtGui.QMainWindow):
	def __init__(self):
		super(QuitButton,self).__init__()
		#self.setGeometry(300,300,250,150)
		self.resize(250,150)
		self.center()
		self.setWindowTitle("hello world!")

		quit = QtGui.QPushButton('Close',self)
		quit.setGeometry(50,50,50,25)

		self.statusBar().showMessage("ready")
		self.connect(quit,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))

		exit = QtGui.QAction(QtGui.QIcon('C:/Python27/code/images/icon.gif'),'Quit',self)
		exit.setShortcut('Ctrl+Q')
		exit.setStatusTip('Exit application')
		self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

		menubar = self.menuBar()
		file = menubar.addMenu('&File')
		file.addAction(exit)

		textEdit = QtGui.QTextEdit()
		self.setCentralWidget(textEdit)

		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(exit)

	def closeEvent(self,event):
		reply = QtGui.QMessageBox.question(self,'Message','Are you sure to quit?',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)

		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


class Example(QtGui.QWidget):
	def __init__(self):
		super(Example,self).__init__()
		self.initUi()

	def initUi(self):
		label1 = QtGui.QLabel('Zetcode',self)
		label1.move(15,10)

		label2 = QtGui.QLabel('tutorials for programmers',self)
		label2.move(35,40)

		self.setWindowTitle('Absolute')
		self.resize(250,150)


class Example2(QtGui.QWidget):
	def __init__(self):
		super(Example2,self).__init__()
		self.initUi()

	def initUi(self):
		okButton = QtGui.QPushButton('ok')
		cancelButton = QtGui.QPushButton('cancel')

		hbox = QtGui.QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(okButton)
		hbox.addWidget(cancelButton)

		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)

		self.setLayout(vbox)
		self.setWindowTitle('box layout')
		self.resize(300,150)


# class Example3(QtGui.QWidget):
# 	def __init__(self):
# 		super(Example3,self).__init__()
# 		self.initUi()

# 	def initUi(self):
# 		self.setWindowTitle('grid layout')

#         names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/',
#             '4', '5', '6', '*', '1', '2', '3', '-',
#             '0', '.', '=', '+']

#         grid = QtGui.QGridLayout()

#         j = 0
#         pos = [(0, 0), (0, 1), (0, 2), (0, 3),
#                 (1, 0), (1, 1), (1, 2), (1, 3),
#                 (2, 0), (2, 1), (2, 2), (2, 3),
#                 (3, 0), (3, 1), (3, 2), (3, 3 ),
#                 (4, 0), (4, 1), (4, 2), (4, 3)]

#         for i in names:
#         	button = QtGui.QPushButton(i)

#         	if j == 2:
#         		grid.addWidget(QtGui.QLabel(''),0,2)
#         	else:
#         		grid.addWidget(button,pos[j][0],pos[j][1])

#         	j = j+1

#         self.setLayout(grid)


class Example4(QtGui.QWidget):
	def __init__(self):
		super(Example4,self).__init__()
		self.initUi()

	def initUi(self):
		title = QtGui.QLabel('title')
		author = QtGui.QLabel('author')
		review = QtGui.QLabel('review')

		titleEdit = QtGui.QLineEdit()
		authorEdit = QtGui.QLineEdit()
		reviewEdit = QtGui.QTextEdit()

		grid = QtGui.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(title,1,0)
		grid.addWidget(titleEdit,1,1)

		grid.addWidget(author,2,0)
		grid.addWidget(authorEdit,2,1)

		grid.addWidget(review,3,0)
		grid.addWidget(reviewEdit,3,1,5,1)

		self.setLayout(grid)

		self.setWindowTitle('hello world!')
		self.resize(350,150)


class Example5(QtGui.QWidget):
	def __init__(self):
		super(Example5,self).__init__()
		self.initUi()

	def initUi(self):
		lcd = QtGui.QLCDNumber(self)
		slider = QtGui.QSlider(QtCore.Qt.Horizontal,self)

		vbox = QtGui.QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(slider)

		self.setLayout(vbox)
		self.connect(slider,QtCore.SIGNAL('valueChanged(int)'),lcd,QtCore.SLOT('display(int)'))

		self.setWindowTitle('SIGNAL & SLOT')
		self.resize(250,150)

	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Escape:
			self.close()


class Example6(QtGui.QMainWindow):
	def __init__(self):
		super(Example6,self).__init__()
		self.initUi()

	def initUi(self):
		button1 = QtGui.QPushButton("Button 1",self)
		button1.move(30,50)

		button2 = QtGui.QPushButton("Button 2",self)
		button2.move(150,50)

		self.connect(button1,QtCore.SIGNAL('clicked()'),self.buttonClicked)
		self.connect(button2,QtCore.SIGNAL('clicked()'),self.buttonClicked)

		self.statusBar().showMessage('ready')
		self.setWindowTitle('Event sender')

		self.resize(290,150)

	def buttonClicked(self):
		sender = self.sender()
		self.statusBar().showMessage(sender.text()+'was pressed')


class Example7(QtGui.QWidget):
	def __init__(self):
		super(Example7,self).__init__()
		self.initUi()

	def initUi(self):
			self.connect(self,QtCore.SIGNAL('closeEmitApp()'),QtCore.SLOT('close()'))
			self.setWindowTitle('emit')
			self.resize(250,150)

	def mousePressEvent(self,event):
		self.emit(QtCore.SIGNAL('closeEmitApp()'))


class Example8(QtGui.QWidget):
	def __init__(self):
		super(Example8,self).__init__()
		self.initUi()

	def initUi(self):
		self.button = QtGui.QPushButton('Dialog',self)
		self.button.setFocusPolicy(QtCore.Qt.NoFocus)

		self.button.move(20,20)
		self.connect(self.button,QtCore.SIGNAL('clicked()'),self.showDialog)
		self.setFocus()

		self.label = QtGui.QLineEdit(self)
		self.label.move(130,22)

		self.setWindowTitle("InputDialog")
		self.setGeometry(300,300,350,80)

	def showDialog(self):
		text,ok = QtGui.QInputDialog.getText(self,'Input Dialog','Enter your name:')

		if ok:
			self.label.setText(str(text))


class Example9(QtGui.QWidget):
	def __init__(self):
		super(Example9,self).__init__()
		self.initUi()

	def initUi(self):
		color = QtGui.QColor(0,0,0)

		self.button = QtGui.QPushButton('Dialog',self)
		self.button.setFocusPolicy(QtCore.Qt.NoFocus)
		self.button.move(20,20)

		self.connect(self.button,QtCore.SIGNAL('clicked()'),self.showDialog)
		self.setFocus()

		self.widget = QtGui.QWidget(self)
		self.widget.setStyleSheet("QWidget {background-color:%s}" %color.name())
		self.widget.setGeometry(130, 22, 100, 100)

		self.setWindowTitle('colorDialog')
		self.setGeometry(300,300,250,180)

	def showDialog(self):
		col = QtGui.QColorDialog.getColor()

		if col.isValid():
			self.widget.setStyleSheet("QWidget {background-color:%s}" %col.name())


class Example10(QtGui.QWidget):
	def __init__(self):
		super(Example10,self).__init__()
		self.initUi()

	def initUi(self):
		hbox = QtGui.QHBoxLayout()

		button = QtGui.QPushButton('Dialog',self)
		button.setFocusPolicy(QtCore.Qt.NoFocus)
		button.move(20,20)

		hbox.addWidget(button)

		self.connect(button,QtCore.SIGNAL('clicked()'),self.showDialog)

		self.label = QtGui.QLabel('Knowledge only matters', self)
		self.label.move(130,20)

		hbox.addWidget(self.label,1)
		self.setLayout(hbox)

		self.setWindowTitle("FontDialog")
		self.setGeometry(300,300,250,110)

	def showDialog(self):
		font,ok = QtGui.QFontDialog.getFont()
		if ok:
			self.label.setFont(font)


class Example11(QtGui.QMainWindow):
	def __init__(self):
		super(Example11,self).__init__()
		self.initUi()

	def initUi(self):
		self.textEdit = QtGui.QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()
		self.setFocus()

		self.button = QtGui.QPushButton('open',self)
		self.connect(self.button,QtCore.SIGNAL('clicked()'),self.showDialog)

	def showDialog(self):
		filename = QtGui.QFileDialog.getOpenFileName(self,'open file','C:/python27')
		fname = open(filename,'r')
		data = fname.read()
		self.textEdit.setText(data)


class Example12(QtGui.QWidget):
	def __init__(self):
		super(Example12,self).__init__()
		self.initUi()

	def initUi(self):
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('checkbox')

		self.cb = QtGui.QCheckBox('show title',self)
		self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
		self.cb.move(10,10)
		self.cb.toggle()
		self.connect(self.cb,QtCore.SIGNAL('stateChanged(int)'),self.changeTitle)

	def changeTitle(self,value):
		if self.cb.isChecked():
			self.setWindowTitle('checkbox')
		else:
			self.setWindowTitle('')


class Example13(QtGui.QWidget):
	def __init__(self):
		super(Example13,self).__init__()
		self.initUi()

	def initUi(self):
		self.color = QtGui.QColor(0,0,0)

		self.red = QtGui.QPushButton('Red',self)
		self.red.setCheckable(True)
		self.red.move(10,10)

		self.connect(self.red,QtCore.SIGNAL('clicked()'),self.setColor)

		self.green = QtGui.QPushButton('Green',self)
		self.green.setCheckable(True)
		self.green.move(10,60)

		self.connect(self.green,QtCore.SIGNAL('clicked()'),self.setColor)

		self.blue = QtGui.QPushButton('Blue',self)
		self.blue.setCheckable(True)
		self.blue.move(10,110)

		self.connect(self.blue,QtCore.SIGNAL('clicked()'),self.setColor)

		self.square = QtGui.QWidget(self)
		self.square.setGeometry(150,20,100,100)
		self.square.setStyleSheet("QWidget {background-color:%s}" %self.color.name())

		self.red.setFocusPolicy(QtCore.Qt.NoFocus)
		self.green.setFocusPolicy(QtCore.Qt.NoFocus)
		self.blue.setFocusPolicy(QtCore.Qt.NoFocus)

		self.setWindowTitle("ToggleButton")
		self.setGeometry(300,300,280,170)

	def setColor(self):
		source = self.sender()

		if source.text() == "Red":
			if self.red.isChecked():
				self.color.setRed(255)
			else:
				self.color.setRed(0)
		elif source.text() == "Green":
			if self.green.isChecked():
				self.color.setGreen(255)
			else:
				self.color.setGreen(0)
		else:
			if self.blue.isChecked():
				self.color.setBlue(255)
			else:
				self.color.setBlue(0)

		self.square.setStyleSheet("QWidget {background-color:%s}" %self.color.name())


class Example14(QtGui.QWidget):
	def __init__(self):
		super(Example14,self).__init__()
		self.initUi()

	def initUi(self):
		slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
		slider.setFocusPolicy(QtCore.Qt.NoFocus)
		slider.setGeometry(30, 40, 100, 30)
		self.connect(slider,QtCore.SIGNAL('valueChanged(int)'),self.changeValue)

		self.label = QtGui.QLabel(self)
		self.label.setPixmap(QtGui.QPixmap("C:/Python27/code/images/images.jpeg"))
		self.label.setGeometry(160,40,80,30)

		self.setWindowTitle('slider')
		self.setGeometry(300,300,250,150)

	def changeValue(self,value):
		self.setWindowTitle(str(value))


class Example15(QtGui.QWidget):
	def __init__(self):
		super(Example15,self).__init__()
		self.initUi()

	def initUi(self):
		self.pbar = QtGui.QProgressBar(self)
		self.pbar.setGeometry(30,40,200,25)

		self.button = QtGui.QPushButton('Start',self)
		self.button.setFocusPolicy(QtCore.Qt.NoFocus)
		self.button.move(40,80)

		self.connect(self.button,QtCore.SIGNAL('clicked()'),self.doAction)

		self.timer = QtCore.QBasicTimer()
		self.step = 0

		self.setWindowTitle("ProgressBar")
		self.setGeometry(300,300,250,150)

	def timerEvent(self,event):
		if self.step >= 100:
			self.timer.stop()
			return

		self.step = self.step+1
		self.pbar.setValue(self.step)

	def doAction(self):
		if self.timer.isActive():
			self.timer.stop()
			self.button.setText('Start')
		else:
			self.timer.start(1,self)
			self.button.setText('Stop')


class Example16(QtGui.QWidget):
	def __init__(self):
		super(Example16,self).__init__()
		self.initUi()

	def initUi(self):
		self.cal = QtGui.QCalendarWidget(self)
		self.cal.setGridVisible(True)
		self.cal.move(20,20)

		self.connect(self.cal,QtCore.SIGNAL('selectionChanged()'),self.showDate)

		self.label = QtGui.QLabel(self)
		date = self.cal.selectedDate()
		self.label.setText(str(date.toPyDate()))
		self.label.move(130,260)

		self.setWindowTitle('calendar')
		self.setGeometry(300,300,350,300)

	def showDate(self):
		date = self.cal.selectedDate()
		self.label.setText(str(date.toPyDate()))


class Example17(QtGui.QWidget):
	def __init__(self):
		super(Example17,self).__init__()
		self.initUi()

	def initUi(self):
		hbox = QtGui.QHBoxLayout(self)
		pixmap = QtGui.QPixmap("C:/Python27/code/images/images.jpeg")

		label = QtGui.QLabel(self)
		label.setPixmap(pixmap)

		hbox.addWidget(label)
		self.setLayout(hbox)

		self.setWindowTitle("photo")
		self.move(250,200)



class Example18(QtGui.QWidget):
	def __init__(self):
		super(Example18,self).__init__()
		self.initUi()

	def initUi(self):
		self.label = QtGui.QLabel(self)
		edit = QtGui.QLineEdit(self)

		edit.move(0,100)
		self.label.move(0,40)

		self.connect(edit,QtCore.SIGNAL('textChanged(QString)'),self.onChanged)

		self.setGeometry(250,200,350,250)

	def onChanged(self,text):
		self.label.setText(text)
		self.label.adjustSize()


class Example19(QtGui.QWidget):
	def __init__(self):
		super(Example19,self).__init__()
		self.initUi()

	def initUi(self):
		hbox = QtGui.QHBoxLayout(self)

		topleft = QtGui.QFrame(self)
		topleft.setFrameShape(QtGui.QFrame.StyledPanel)

		topcenter = QtGui.QFrame(self)
		topcenter.setFrameShape(QtGui.QFrame.StyledPanel)

		topright = QtGui.QFrame(self)
		topright.setFrameShape(QtGui.QFrame.StyledPanel)

		bottom = QtGui.QFrame(self)
		bottom.setFrameShape(QtGui.QFrame.StyledPanel)

		splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
		splitter1.addWidget(topleft)
		splitter1.addWidget(topcenter)
		splitter1.addWidget(topright)

		splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
		splitter2.addWidget(splitter1)
		splitter2.addWidget(bottom)

		hbox.addWidget(splitter2)
		self.setLayout(hbox)

		self.setWindowTitle('QSplitter')
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

		self.setGeometry(250,200,350,250)


class Example20(QtGui.QWidget):
	def __init__(self):
		super(Example20,self).__init__()
		self.initUi()

	def initUi(self):
		self.label = QtGui.QLabel("Ubuntu",self)

		combo = QtGui.QComboBox(self)
		combo.addItem("Ubuntu")
		combo.addItem("Mandriva")
		combo.addItem("Fedora")
		combo.addItem("Red Hat")
		combo.addItem("Gentoo")

		combo.move(50,50)
		self.label.move(50,150)

		self.connect(combo,QtCore.SIGNAL("activated(QString)"),self.onActivated)
		self.setGeometry(250,200,350,250)

		self.setWindowTitle("QComboBox")

	def onActivated(self,text):
		self.label.setText(text)
		self.label.adjustSize()


class Button(QtGui.QPushButton):
	def __init__(self,title,parent):
		super(Button,self).__init__(title,parent)
		self.setAcceptDrops(True)

	def dragEnterEvent(self,e):
		if e.mimeData().hasFormat("text/plain"):
			e.accept()
		else:
			e.ignore()

	def dropEvent(self, e):
		self.setText(e.mimeData().text())


class Example21(QtGui.QWidget):
	def __init__(self):
		super(Example21,self).__init__()
		self.initUi()

	def initUi(self):
		edit = QtGui.QLineEdit('',self)
		edit.setDragEnabled(True)
		edit.move(30,65)

		button = Button("Button",self)
		button.adjustSize()
		button.move(190,65)

		self.setWindowTitle("Simple Drap & Drop")
		self.setGeometry(300,300,300,150)


class B(QtGui.QPushButton):
	def __init__(self,title,parent):
		super(B,self).__init__(title,parent)

	def mouseMoveEvent(self,e):
		if e.buttons() != QtCore.Qt.RightButton:
			return

		mimeData = QtCore.QMimeData()

		drag = QtGui.QDrag(self)
		drag.setMimeData(mimeData)
		drag.setHotSpot(e.pos()-self.rect().topLeft())
		dropAction = drag.start(QtCore.Qt.MoveAction)
		print e.pos

	def mousePressEvent(self,e):
		QtGui.QPushButton.mousePressEvent(self,e)
		if e.button() == QtCore.Qt.LeftButton:
			print 'press'


class Example22(QtGui.QWidget):
	def __init__(self):
		super(Example22,self).__init__()
		self.initUi()

	def initUi(self):
		self.setAcceptDrops(True)

		self.button = B('Button',self)
		self.button.move(100,65)
		self.button.setFocusPolicy(QtCore.Qt.NoFocus)

		self.setWindowTitle('Click or move')
		self.setGeometry(300,300,280,150)

	def dragEnterEvent(self,e):
		e.accept()

	def dropEvent(self,e):
		position = e.pos()
		self.button.move(position)

		e.setDropAction(QtCore.Qt.MoveAction)
		e.accept()


class Example23(QtGui.QWidget):
	def __init__(self):
		super(Example23,self).__init__()
		self.initUi()

	def initUi(self):
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Draw Text')

		self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
  \u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
  \u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

 	def paintEvent(self,event):
 		qp = QtGui.QPainter()
 		qp.begin(self)
 		self.drawText(event,qp)
 		qp.end()

 	def drawText(self,event,qp):
 		qp.setPen(QtGui.QColor(168,34,3))
 		qp.setFont(QtGui.QFont('Decorative',10))
 		qp.drawText(event.rect(),QtCore.Qt.AlignCenter,self.text)


class Example24(QtGui.QWidget):

    def __init__(self):
        super(Example24, self).__init__()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Points')

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):

        qp.setPen(QtCore.Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)


class Example25(QtGui.QWidget):

    def __init__(self):
        super(Example25, self).__init__()

        self.setGeometry(300, 300, 350, 280)
        self.setWindowTitle('Colors')

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)

        self.drawRectangles(qp)

        qp.end()

    def drawRectangles(self, qp):

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(255, 0, 0, 80))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QtGui.QColor(255, 0, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QtGui.QColor(255, 0, 0, 255))
        qp.drawRect(250, 15, 90, 60)

        qp.setBrush(QtGui.QColor(10, 163, 2, 55))
        qp.drawRect(10, 105, 90, 60)

        qp.setBrush(QtGui.QColor(160, 100, 0, 255))
        qp.drawRect(130, 105, 90, 60)

        qp.setBrush(QtGui.QColor(60, 100, 60, 255))
        qp.drawRect(250, 105, 90, 60)

        qp.setBrush(QtGui.QColor(50, 50, 50, 255))
        qp.drawRect(10, 195, 90, 60)

        qp.setBrush(QtGui.QColor(50, 150, 50, 255))
        qp.drawRect(130, 195, 90, 60)

        qp.setBrush(QtGui.QColor(223, 135, 19, 255))
        qp.drawRect(250, 195, 90, 60)



class Example26(QtGui.QWidget):

    def __init__(self):
        super(Example26, self).__init__()

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('penstyles')

    def paintEvent(self, e):

        qp = QtGui.QPainter()

        qp.begin(self)
        self.doDrawing(qp)
        qp.end()

    def doDrawing(self, qp):

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(QtCore.Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(QtCore.Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(QtCore.Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(QtCore.Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(QtCore.Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)


class Example27(QtGui.QWidget):

    def __init__(self):
        super(Example27, self).__init__()

        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')

    def paintEvent(self, e):

        qp = QtGui.QPainter()

        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):

        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(QtCore.Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(QtCore.Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(QtCore.Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush.setStyle(QtCore.Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(QtCore.Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush.setStyle(QtCore.Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)


class BurningWidget(QtGui.QWidget):

    def __init__(self):
        super(BurningWidget, self).__init__()

        self.initUI()

    def initUI(self):

        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

        self.connect(self, QtCore.SIGNAL("updateBurningWidget(int)"),
            self.setValue)


    def setValue(self, value):

        self.value = value


    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()


    def drawWidget(self, qp):

        font = QtGui.QFont('Serif', 7, QtGui.QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10.0))


        till = int(((w / 750.0) * self.value))
        full = int(((w / 750.0) * 700))

        if self.value >= 700:
            qp.setPen(QtGui.QColor(255, 255, 255))
            qp.setBrush(QtGui.QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QtGui.QColor(255, 175, 175))
            qp.setBrush(QtGui.QColor(255, 175, 175))
            qp.drawRect(full, 0, till-full, h)
        else:
            qp.setPen(QtGui.QColor(255, 255, 255))
            qp.setBrush(QtGui.QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)


        pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1,
            QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(QtCore.Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)

        j = 0

        for i in range(step, 10*step, step):

            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i-fw/2, h/2, str(self.num[j]))
            j = j + 1


class Example28(QtGui.QWidget):

    def __init__(self):
        super(Example28, self).__init__()

        self.initUI()

    def initUI(self):

        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.setRange(1, 750)
        slider.setValue(75)
        slider.setGeometry(30, 40, 150, 30)

        self.wid = BurningWidget()

        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'),
            self.changeValue)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Burning')

    def changeValue(self, value):

        self.wid.emit(QtCore.SIGNAL("updateBurningWidget(int)"), value)
        self.wid.repaint()


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)

	ex = Example28()
	ex.show()

	sys.exit(app.exec_())


