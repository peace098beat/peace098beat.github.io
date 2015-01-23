# -*- coding: utf-8 -*-
"""
ButtonBoxWidget

PyQt4 Tutorial
http://www.slideshare.net/RansuiIso/pyqtgui

Created on Thu Jan 22 14:43:19 2015
@author: 0160929
"""
import sys
import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import random


class ButtonBoxWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        # コンストラクタ
        QtGui.QWidget.__init__(self, parent=parent)
        # 実際の生成コード
        self.setup_ui()

    def setup_ui(self):
        # QPushButtonのインスタンスを作る
        self.start_button = QtGui.QPushButton("START", parent=self)
        self.stop_button = QtGui.QPushButton("STOP", parent=self)
        self.reset_button = QtGui.QPushButton("RESET", parent=self)
        self.quit_button = QtGui.QPushButton("QUIT", parent=self)

        # Buttonをレイアウトマネージャに入れる
        layout = QtGui.QGridLayout()
        layout.addWidget(self.start_button, 0, 0)
        layout.addWidget(self.stop_button, 0, 1)
        layout.addWidget(self.reset_button, 1, 0)
        layout.addWidget(self.quit_button, 1, 1)
        
        # レイアウトマネージャをWidgetに入れる
        self.setLayout(layout)


class CountDownWidget(QtGui.QWidget):
    
    def __init__(self, parent=None):
        # コンストラクタ
        QtGui.QWidget.__init__(self, parent=parent)
        self.interval = 10        
        self.setup_ui()
        
    def setup_ui(self):
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, 
                           QtGui.QSizePolicy.Expanding)
        self.timer = QtCore.QTimer(parent=self)
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.do_countdown)
        
        self.lcd_number = QtGui.QLCDNumber(parent=self)
        self.lcd_number.setSizePolicy(QtGui.QSizePolicy.Expanding, 
                                      QtGui.QSizePolicy.Expanding)
        self.lcd_number.setFrameStyle(QtGui.QFrame.NoFrame)
        self.lcd_number.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_number.setDigitCount(6)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.lcd_number)
        self.setLayout(layout)
        
        self.reset_count()
        
    def update_display(self):
        self.lcd_number.display("%6.2f" % (self.count / 100))
        self.lcd_number.update()
    
    def do_countdown(self):
        self.count -= 1
        self.update_display()
        if self.count <= 0:
            self.stop_countdown()
            
    def start_countdown(self):
        if self.count > 0:
            self.timer.start()
            
    def stop_countdown(self):
        self.timer.stop()
        
    def reset_count(self):
        self.count = 18000
        self.update_display()
        
        
class GraphPanelWidget(QtGui.QWidget):
    #self.panelsize = [300 ,200]
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.setup_ui()
    
    def setup_ui(self):
        # self.graph_panel = QtGui.QPainter()
        # self.setGeometry(300, 300, 280, 170)
        # self.show()
        # self.start_button = QtGui.QPushButton("START", parent=self)
        self.setFixedSize(320, 320)
        # self.label = QtGui.QLabel('graph', self)
        
        # Buttonをレイアウトマネージャに入れる
        layout = QtGui.QVBoxLayout()
        # layout.addWidget(self.label)   
        # layout.addWidget(self.start_button)
    
        # レイアウトマネージャをWidgetに入れる
        self.setLayout(layout)
        
    """ PAINT EVENT """
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        # self.drawRandomPoints(qp)
        #self.drawOnePoints(qp,e)
        qp.end()
        
    def drawRandomPoints(self, qp):
        qp.setPen(QtCore.Qt.red)
        size = self.size()
        
        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)
            
    def drawOnePoints(self, qp, e):
        #x=e.x()
        #y=e.y()
        x=3
        y=50
        qp.setPen(QtCore.Qt.red)
        qp.drawPoint(x,y)        
        
    def mousePressEvent(self, e):
        print("mouse press (x,y)=(%d, %d)" % (e.x(),e.y()))
        # self.paintEvent(e)
        # self.plotPoint(e.x(),e.y())
        self.lastpos = e.pos()
        
    def mouseReleaseEvent(self, e):
        print("mouse Release (x,y)=(%d, %d)" % (e.x(),e.y()))

    def mouseDoubleClickEvent(self, e):
        print("mouseDoubleClick")   
        
    def mouseMoveEvent(self, e):
        print("mouseMove=" + bin(int(e.buttons())))
        qp = QtGui.QPainter()
        qbuffer = QtGui.QPainter()
        
        qp.begin(self)
        
        
    def weelEvent(self, e):
        print("mouseWeel=")
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    panel = QtGui.QWidget()
    
    """ 子Widget """
    countdown_widget = CountDownWidget(parent=panel)
    button_box_widget = ButtonBoxWidget(parent=panel)
    graph_panel_widget = GraphPanelWidget(parent=panel)

    """ レイアウトマネージャ """    
    panel_layout = QtGui.QVBoxLayout()
    panel_layout.addWidget(countdown_widget)
    panel_layout.addWidget(button_box_widget)
    panel_layout.addWidget(graph_panel_widget)

    """ Panel Widget """
    panel.setLayout(panel_layout)
    #panel.setFixedSize(320, 200)
    
    """ Main Window """
    main_window = QtGui.QMainWindow()
    main_window.setWindowTitle("Ramen Timer")
    main_window.setCentralWidget(panel)
    
    main_window.show()
    
    """ Conectivity """
    button_box_widget.start_button.clicked.connect(countdown_widget.start_countdown)
    button_box_widget.stop_button.clicked.connect(countdown_widget.stop_countdown)
    button_box_widget.reset_button.clicked.connect(countdown_widget.reset_count)
    button_box_widget.quit_button.clicked.connect(app.quit)
    
    app.exec_()
    
if __name__ == '__main__':
    print("app main start")
    main()
    