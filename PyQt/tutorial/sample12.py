# -*- coding: utf-8 -*-
"""
ButtonBoxWidget

PyQt4 Tutorial
http://www.slideshare.net/RansuiIso/pyqtgui

Created on Thu Jan 22 14:43:19 2015
@author: 0160929
"""
import PyQt4.QtGui

class ButtonBoxWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        # コンストラクタ
        QtGui.Qwidget.__init__(self, parent=parent)
        # 実際の生成コード
        self.setup_ui()

    def setUP_ui(self):
        # QPushButtonのインスタンスを作る
        self.start_button = QPushButton("START", parent=self)
        self.stop_button = QPushButton("STOP", parent=self)
        self.reset_button = QPushButton("RESET", parent=self)
        self.quit_button = QPushButton("QUIT", parent=self)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.start_button, 0, 0)
        layout.addWidget(self.stop_button, 0, 1)
        layout.addWidget(self.reset_button, 1, 0)
        layout.addWidget(self.quit_button, 1, 1)

        self.setLayout(layout)
