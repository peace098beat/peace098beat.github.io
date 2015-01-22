
# Python初心者が、１日でPyQtを使って数値計算用のGUIアプリを作成する

## 事前調査

PyQtとは
>PyQtは、クロスプラットフォームなGUIツールキットであるQtのPythonバインディングにして、PythonでGUIプログラミングをするときの選択肢の一つである。PyQtの他には、PySide・PyGTK・wxPython・TkinterなどのGUIツールキットが存在する。Qtと同様にPyQtはフリーソフトウェアである。PyQtはPythonのプラグインとして実装されている。PyQtはクロスプラットフォームなツールキットであり、Windows・Linux・OS Xなどをサポートしている[4]。

Python本家のPyQtページ
https://wiki.python.org/moin/PyQt4

PyQt4 Reference Guide
http://pyqt.sourceforge.net/Docs/PyQt4/

PyQt5 Reference Guide
http://pyqt.sourceforge.net/Docs/PyQt5/

## インストール・チュートリアル関連

PyQtで始めるGUIプログラミング  
http://www.slideshare.net/RansuiIso/pyqtgui

PyQtのインストールと動作確認
https://blog.ymyzk.com/2014/11/mac-os-x-pyqt/

Python GUI PyQt もっと早く使っておけばよかった  
(windowsへのインストール方法と、サンプルコードの紹介)  
http://typea.info/blg/glob/2014/08/python-gui-pyqt.html

PyQtのサンプル多数  
http://www.not-enough.org/abe/manual/api-aa09/pyqt1.html

ZetCode(いろいろな言語のチュートリアルが掲載されている)  
http://zetcode.com/

## 励みになる資料

光学設計者の学習メモ  
http://retrofocus28.blogspot.jp/search/label/pyqt

## 環境整備編

### 環境条件

	$ uname -a
	Darwin nohara-no-MacBook-Air.local 13.4.0 
	Darwin Kernel Version 13.4.0:
	Sun Aug 17 19:50:11 PDT 2014; 
	oot:xnu-2422.115.4~1/RELEASE_X86_64 x86_64

	$ python
	Python 2.7.5

	>>> import numpy 
	>>> numpy.__version__
	'1.6.2'

	>>> import scipy
	>>> scipy.__version__
	'0.11.0'
	>>> 

### PyQt5のインストール

	# 1. PyQt5 の依存である sip をインストール
	brew install sip

	# 2. PyQt5 を python2.7 でビルド，インストール (python3 だとエラーになります)
	brew install pyqt5 --with-python --without-python3

	# 3. PYTHONPATH の追加
	export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH

	(~/.bashrcへ書き込み)
	echo export PYTHONPATH=/usr/local/lib/python2.7/site-packages:"$PYTHONPATH" > ~/.bashrc

	# 4. インストールに成功したかチェック
	$ python
	>>> import PyQt5
	>>> PyQt5
	>>> <module 'PyQt5' from '/usr/local/lib/python2.7/site-packages/PyQt5/__init__.py'>


## エラー対策

### PyQtのインストールでエラー

	# 2. PyQt5 を python2.7 でビルド，インストール (python3 だとエラーになります)
	brew install pyqt5 --with-python --without-python3

エラー文

	Querying qmake about your Qt installation...
	Determining the details of your Qt installation...
	/usr/local/Cellar/qt5/5.4.0/bin/qmake -o qtdetail.mk qtdetail.pro
	xcode-select: error: tool 'xcodebuild' requires Xcode, but active developer directory '/Library/Developer/CommandLineTools' is a command line tools instance
	Project ERROR: Could not resolve Xcode version.
	Warning: It appears you have MacPorts or Fink installed.
	Software installed with other package managers causes known problems for
	Homebrew. If a formula fails to build, uninstall MacPorts/Fink and try again.

	READ THIS: http://git.io/brew-troubleshooting

xcodeがなさそう

Xcodeをインストール後実行

	brew install pyqt5 --with-python --without-python3
	==> Downloading https://downloads.sf.net/project/pyqt/PyQt5/PyQt-5.4/PyQt-gpl-5.
	Already downloaded: /Library/Caches/Homebrew/pyqt5-5.4.tar.gz
	==> Patching
	==> python configure.py --confirm-license --bindir=/usr/local/Cellar/pyqt5/5.4/b
	==> make
	==> make install
	==> make clean
	==> Caveats
	Python modules have been installed and Homebrew's site-packages is not
	in your Python sys.path, so you will not be able to import the modules
	this formula installed. If you plan to develop with these modules,
	please run:
	  mkdir -p /Users/noharatomoyuki/Library/Python/2.7/lib/python/site-packages
	  echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> /Users/noharatomoyuki/Library/Python/2.7/lib/python/site-packages/homebrew.pth
	==> Summary
	🍺  /usr/local/Cellar/pyqt5/5.4: 726 files, 22M, built in 21.6 minutes

インストール成功




