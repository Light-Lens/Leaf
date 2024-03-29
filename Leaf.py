# Leaf
# Modules are imported that will be used in Leaf browser.
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# These are other modules that are imported for Leaf.
from urllib.parse import urlparse
import sys, os

# Initializing Leaf browser
class Leaf(QMainWindow):
	def __init__(self): 
		super(Leaf, self).__init__()

		# Setting up window
		self.setWindowTitle("Leaf")
		self.showMaximized()

		# Opening Google
		self.browser = QWebEngineView()
		self.browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
		self.browser.page().fullScreenRequested.connect(lambda request: request.accept())
		self.browser.setUrl(QUrl("https://www.google.com"))
		self.browser.urlChanged.connect(self.update_urlbar)
		self.browser.loadFinished.connect(self.update_title)
		self.browser.setContextMenuPolicy(Qt.NoContextMenu)
		self.setCentralWidget(self.browser)


		# Adding a toolbar to Leaf
		self.Toolbar = QToolBar("Navigation")
		self.Toolbar.setIconSize(QSize(17, 17))
		self.Toolbar.setMovable(False)
		self.Toolbar.setFixedHeight(40)
		self.Toolbar.setStyleSheet("background: #111111;")
		self.addToolBar(self.Toolbar)

		self.back_btn = QAction(QIcon(os.path.join("res", "Arrow-Back.png")), "Go Back One Page", self)
		self.back_btn.setStatusTip("Go Back One Page")
		self.back_btn.triggered.connect(self.browser.back)
		self.Toolbar.addAction(self.back_btn)

		self.forward_btn = QAction(QIcon(os.path.join("res", "Arrow-Forward.png")), "Go Forward One Page", self)
		self.forward_btn.setStatusTip("Go Forward One Page")
		self.forward_btn.triggered.connect(self.browser.forward)
		self.Toolbar.addAction(self.forward_btn)

		self.reload_btn = QAction(QIcon(os.path.join("res", "Reload.png")), "Reload Current Page", self)
		self.reload_btn.setStatusTip("Reload Current Page")
		self.reload_btn.triggered.connect(self.browser.reload)
		self.Toolbar.addAction(self.reload_btn)

		self.home_btn = QAction(QIcon(os.path.join("res", "Home.png")), "Leaf Home Page", self)
		self.home_btn.setStatusTip("Leaf Home Page")
		self.home_btn.triggered.connect(self.Go_HOME)
		self.Toolbar.addAction(self.home_btn)

		self.urlbar = QLineEdit()
		self.font = self.urlbar.font()
		self.font.setPointSize(11)
		self.urlbar.setStyleSheet(
			"""
			QLineEdit
			{
				color: #9f9f9f;
				background-color: #1a1a1a;
				border: none;
				border-radius: 3px;
				padding-left: 25px;
				font-family: Calibri;
			}
			QLineEdit:hover
			{
				color: #f9f9f9;
				background-color: #2c2c2c;
			}
			QLineEdit:focus
			{
				color: #f9f9f9;
				background-color: #2c2c2c;
			}
			"""
			)
		self.urlbar.setFixedHeight(30)
		self.urlbar.returnPressed.connect(self.navigate_to_url)
		self.Toolbar.addWidget(self.urlbar)
		self.urlbar.setFont(self.font)

		self.stop_btn = QAction(QIcon(os.path.join("res", "Stop.png")), "Stop loading Current Page", self)
		self.stop_btn.setStatusTip("Stop loading Current Page")
		self.stop_btn.triggered.connect(self.browser.stop)
		self.Toolbar.addAction(self.stop_btn)
		self.setStyleSheet("""
			QMenu
			{
				padding-top: 10px;
				padding-bottom: 10px;
				color: #f9f9f9;
				background: #1a1a1a;
				width: 300px;
				font-size: 15px;
				font-family: Calibri;
			}
			QMenu::item:selected
			{
				background: #2c2c2c;
			}"""
			)

	def contextMenuEvent(self, event):
		self.menu = QMenu(self)

		self.menu.addAction("Back", self.browser.back)
		self.menu.addAction("Forward", self.browser.forward)
		self.menu.addAction("Reload", self.browser.reload)
		self.menu.addSeparator()
		self.menu.addAction("View page source")
		self.menu.addAction("Inspect")

		self.menu.exec_(event.globalPos())

	# Open Google (Home page for Leaf)
	def Go_HOME(self): self.browser.setUrl(QUrl("https://www.google.com"))

	# Update title of the window
	def update_title(self):
		Title = self.browser.page().title()
		self.setWindowTitle(f"{Title} - Leaf")

	# Navigate to url
	def navigate_to_url(self):
		q = QUrl(self.urlbar.text())
		if q.scheme() == "": q.setScheme("http")

		self.browser.setUrl(QUrl(q))

	# Update urlbar
	def update_urlbar(self, q):
		self.urlbar.setText(q.toString())
		self.urlbar.setCursorPosition(0)

# Setup Leaf
if __name__ == '__main__':
	app = QApplication(sys.argv)
	# app.setApplicationName("Leaf")
	# app.setOrganizationName("Light-Lens")
	# app.setOrganizationDomain("https://github.com/Light-Lens")
	Leaf = Leaf()
	Leaf.show()
	app.exec_()
