# -*- coding: utf-8 -*-
"""
PyQt4 Tutorial
http://www.slideshare.net/RansuiIso/pyqtgui

Created on Thu Jan 22 14:43:19 2015
@author: 0160929
"""

import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

def on_click():
    print("click")

def on_press():
    print("press")

def on_release():
    print("release")

def print_state(state):
    if state == 0:
        print("Unchecked")
    else:
        print("Checked")

def main():
    # QApplication()
    # QtのGUIプログラム全体をコントロールする。
    # コマンドライン引数sys.argvを渡す
    app = QtGui.QApplication(sys.argv)
    
    # QMainWindow()
    # メインウィンドウを表現する
    main_window = QtGui.QMainWindow()
    
    # QPushButton()
    # 基本的なボタンコンポーネント
    hello_button = QtGui.QPushButton("Hello World")
    # connect()
    # ボタン押下時に発生するイベントを教える
    hello_button.clicked.connect(on_click)
    hello_button.pressed.connect(on_press)
    hello_button.released.connect(on_release)
    
    # setCentralWidget()
    # センター配置用のウィジェットにボタンを配置
    main_window.setCentralWidget(hello_button)
    
    # show()
    # GUI App を実行    
    main_window.show()
    
    # exec_()
    # イベントループを開始するメソッド
    app.exec_()
    
if __name__ == '__main__':
    main()