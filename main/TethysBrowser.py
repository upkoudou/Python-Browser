from PyQt5.QtWebEngine import * 
from PyQt5.QtGui import * 
from PyQt5.QtDesigner import * 
from PyQt5.QtCore import * 
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.QtWidgets import *

class TethysBrowser(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(TethysBrowser, self).__init__(*args, **kwargs)
        
        self.window = QWidget()
        self.window.setWindowTitle("Tethys Browser")
        
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)
        
        self.go_btn = QPushButton("GO") 
        self.go_btn.setMinimumHeight(30)
        
        self.back_btn = QPushButton("<") 
        self.back_btn.setMinimumHeight(30)
        
        self.fwd_btn = QPushButton(">") 
        self.fwd_btn.setMinimumHeight(30)
        
        self.home_btn = QPushButton("π") 
        self.home_btn.setMinimumHeight(30)
        
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.fwd_btn)
       # self.horizontal.addWidget(self.home_btn)

        self.browser = QWebEngineView()
        
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.fwd_btn.clicked.connect(self.browser.forward)
        self.home_btn.clicked.connect(lambda: self.home())
        
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
                                  
        self.browser.setUrl(QUrl("http://www.tethyseid.com"))
        
        self.window.setLayout(self.layout)
        self.window.show()
        
    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))
        
   # def home(self,url):
   #     url = "http://www.google.com"
   #     self.home_btn.setText(url)
        
               
App = QApplication([])
Window = TethysBrowser()
App.exec()