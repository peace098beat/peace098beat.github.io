#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This program creates a skeleton of
a classic GUI application with a menubar,
toolbar, statusbar and a central widget. 

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011

http://zetcode.com/gui/pyqt4/menusandtoolbars/

"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        # 継承元のコンストラクタ
        super(Example, self).__init__()
        
        self.initUI()
     
    def initUI(self):
        
        """ Text Edit """
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)
  
        """ Define Status Bar """
        self.statusBar()
        self.statusBar().showMessage('Ready')
        
        """ Define Action to Exit """
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
                                
        """ Define MenuBar """
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction) # set to 'Action'
        fileMenu = menubar.addMenu('&Tools')
        fileMenu = menubar.addMenu('&Help')
        
        """ Define Toolbar """
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(exitAction)
          
        """ QMainWindw """  
        wh=150;
        ww=300;
        x=1200;
        y=500;
        self.setGeometry(x,y,ww,wh)
        self.setWindowTitle('Statusbar')
        
        """ Show """
        self.show()
    
        
def main():
    # QtGuiのオブジェクトを作成?
    app = QtGui.QApplication(sys.argv)
    
    # User作成のオブジェクトを生成
    ex = Example()
    
    #システム終了    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()