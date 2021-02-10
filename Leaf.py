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
import platform
import sys
import os

# Initializing Leaf browser
os.system('title Leaf browser')
init(autoreset = True)

# Global variables
System_details = platform.uname()

# Setting up Terminal
print(Fore.GREEN + "Leaf browser")
print(Fore.GREEN + f"Host: {System_details.node}")
print(Fore.GREEN + f"System: {System_details.system} {System_details.release}")
print(Fore.GREEN + f"Processor: {System_details.processor}\n")

# Setting up Leaf class
class Leaf(QMainWindow):
	def __init__(self, *args, **kwargs): 
		super(Leaf, self).__init__(*args, **kwargs)
		# Setting up window
		self.setWindowTitle("Leaf")
		self.setGeometry(25, 25, 1000, 575)

		# Opening Google
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl("http://google.com"))
		self.browser.urlChanged.connect(self.update_urlbar)
		self.browser.loadFinished.connect(self.update_title)
		self.setCentralWidget(self.browser)

		# Adding a toolbar to Leaf
		self.Toolbar = QToolBar("Navigation")
		self.Toolbar.setMovable(False)
		self.Toolbar.setFixedHeight(33)
		self.addToolBar(self.Toolbar)

		self.Home = QPushButton("Home", self)
		self.Home.setStyleSheet("background-color : #f9f9f9")
		self.Home.clicked.connect(self.Go_HOME)
		self.Toolbar.addWidget(self.Home)

		self.Toolbar.addSeparator()

		self.urlbar = QLineEdit()
		self.urlbar.setStyleSheet("background-color : #f9f9f9")
		self.urlbar.setFixedHeight(23)
		self.urlbar.returnPressed.connect(self.navigate_to_url)
		self.Toolbar.addWidget(self.urlbar)

	# Open Google (Home page for Leaf)
	def Go_HOME(self):
		self.browser.setUrl(QUrl("http://google.com"))

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
