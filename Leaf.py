# Leaf
# Modules are imported that will be used in Leaf browser.
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# These are other modules that are imported for Leaf.
from colorama import Fore, Back, Style
from colorama import init
import sys, os

# Initializing Leaf browser
class Leaf(QMainWindow):
	def __init__(self, *args, **kwargs): 
		super(Leaf, self).__init__(*args, **kwargs)
		# Setting up window
		self.setWindowTitle("Leaf")
		self.setWindowIcon(QIcon(".\\res\\Logo.png"))
		self.setGeometry(10, 70, 1000, 575)

		# Opening Google
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl("https://www.google.co.in"))
		self.browser.urlChanged.connect(self.update_urlbar)
		self.browser.loadFinished.connect(self.update_title)
		self.setCentralWidget(self.browser)

		# Adding a toolbar to Leaf
		self.Toolbar = QToolBar("Navigation")
		self.Toolbar.setMovable(False)
		self.Toolbar.setFixedHeight(30)
		self.Toolbar.setStyleSheet("background-color: #1a1a1a")
		self.addToolBar(self.Toolbar)

		self.back_btn = QAction(QIcon(os.path.join('res', 'Arrow-Back.png')), "Go Back One Page", self)
		self.back_btn.setStatusTip("Go Back One Page")
		self.back_btn.triggered.connect(self.browser.back)
		self.Toolbar.addAction(self.back_btn)

		self.forward_btn = QAction(QIcon(os.path.join('res', 'Arrow-Forward.png')), "Go Forward One Page", self)
		self.forward_btn.setStatusTip("Go Forward One Page")
		self.forward_btn.triggered.connect(self.browser.forward)
		self.Toolbar.addAction(self.forward_btn)

		self.reload_btn = QAction(QIcon(os.path.join('res', 'Reload.png')), "Reload Current Page", self)
		self.reload_btn.setStatusTip("Reload Current Page")
		self.reload_btn.triggered.connect(self.browser.reload)
		self.Toolbar.addAction(self.reload_btn)

		self.home_btn = QAction(QIcon(os.path.join('res', 'Home.png')), "Leaf Home Page", self)
		self.home_btn.setStatusTip("Leaf Home Page")
		self.home_btn.triggered.connect(self.Go_HOME)
		self.Toolbar.addAction(self.home_btn)

		self.urlbar = QLineEdit()
		self.font = self.urlbar.font()
		self.font.setPointSize(10)
		self.urlbar.setStyleSheet("color: #f9f9f9; background-color: #3d3d3d; border: none")
		self.urlbar.setFixedHeight(20)
		self.urlbar.returnPressed.connect(self.navigate_to_url)
		self.Toolbar.addWidget(self.urlbar)
		self.urlbar.setFont(self.font)

		self.stop_btn = QAction(QIcon(os.path.join('res', 'Stop.png')), "Stop loading Current Page", self)
		self.stop_btn.setStatusTip("Stop loading Current Page")
		self.stop_btn.triggered.connect(self.browser.stop)
		self.Toolbar.addAction(self.stop_btn)

		self.options_btn = QAction(QIcon(os.path.join('res', 'Options.png')), "Options menu", self)
		self.options_btn.setStatusTip("Options menu")
		self.Toolbar.addAction(self.options_btn)

	# Open Google (Home page for Leaf)
	def Go_HOME(self): self.browser.setUrl(QUrl("https://www.google.co.in"))

	# Update title of the window
	def update_title(self):
		title = self.browser.page().title()
		self.setWindowTitle("%s - Leaf" % title)

	# Navigate to url
	def navigate_to_url(self):
		q = QUrl(self.urlbar.text())
		if q.scheme() == "": q.setScheme("http")
		self.browser.setUrl(q)

	# Update urlbar
	def update_urlbar(self, q):
		self.urlbar.setText(q.toString())
		self.urlbar.setCursorPosition(0)

# Setting up Leaf
if __name__ == '__main__':
	app = QApplication(sys.argv)
	Leaf = Leaf()
	Leaf.show()
	app.exec_()
