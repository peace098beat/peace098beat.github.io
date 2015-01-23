# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 11:42:58 2015

@author: 0160929
"""

import sys
from PyQt4 import QtGui, QtCore
 
class PyQtExample(QtGui.QWidget):
    print 'test'
    
    def __init__(self):
        super(PyQtExample, self).__init__()
        self.initUi()
 
    def initUi(self):
        self.cmbMode = QtGui.QComboBox(self)
        self.cmbMode.addItems(('Item1','Item2','Item3','Item4','Item5'))
        self.cmbMode.move(50,50)
 
        self.chkTblPrefix = QtGui.QCheckBox(u'CheckBox Title',self)
        self.chkTblPrefix.move(50,80)
 
        self.btnExec = QtGui.QPushButton(u'実行',self)
        self.btnExec.move(50,110)
        self.btnExec.clicked.connect(self.doExecute)
 
        self.btnClear = QtGui.QPushButton(u'クリア',self)
        self.btnClear.move(150,110)
        self.btnClear.clicked.connect(self.doClear)
 
        self.txtIn = QtGui.QTextEdit(self)
        self.txtIn.move(50,160)
 
        self.txtOut = QtGui.QTextEdit(self)
        self.txtOut.move(350,160)
 
        self.setGeometry(200, 200, 700, 400)
        self.show()
 
    def doExecute(self, value):
        self.txtOut.append(self.txtIn.toHtml())
 
    def doClear(self, value):
        self.txtOut.clear()
        self.txtIn.clear()
 
def main():
    app = QtGui.QApplication(sys.argv)
    example = PyQtExample()
    sys.exit(app.exec_())

main()
if __name__ == '__main__':
    main()