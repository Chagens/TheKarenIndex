import sys
import requests
import time
from PyQt6 import QtWidgets
from bs4 import BeautifulSoup
#from spellchecker import SpellChecker
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QIcon, QFont, QWindow
from main_ui import Main_UI
from reviewscraper import *
from storing import *
#from file_analysis import *
from word_library import *
class Leader_Window(QWidget):
  def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout(self)
        self.setGeometry(100,100,800, 600)
        self.setWindowTitle('Leaderboard')
        self.setWindowIcon(QIcon('TheKarenIndex.png'))
        self.label = QLabel("Leaderboard")
        self.widget = QWidget(self)
        self.widget.setObjectName("widget")
        
        #match main background
        self.widget.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));"
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 brown, stop:1 gold);}")
        self.widget.setGeometry(0,0,800, 600)
        #area to display leaderboard

        self.l1 = QLabel()
        self.l1.setText("Short dated! First time I have ever received food from Amazon that has been such a short expiration date. So discouraging and disappointing.")
        layout.addWidget(self.l1)
        
class Main_Window(QMainWindow, Main_UI):
    '''
      - It also calls setup_UI to set up the ui
      - The UI is manipulated within main_ui.py
    '''  
    def __init__(self):
        '''
          - Initialize UI with blank values
          - Initialize button to be pressed
        '''
        super(Main_Window, self).__init__()
        self.setWindowIcon(QIcon('TheKarenIndex.png'))
        self.setWindowTitle('The Karen Index')
        self.setup_UI(self)  
        self.Leaderboard_button.pressed.connect(self.display_leaderboard)
        self.Favorite_button.pressed.connect(self.add_Favorites)
        self.Favorites.activated.connect(self.select_favorite)
        self.Themes.activated.connect(self.select_theme)
        self.Categories.activated.connect(self.select_category)
        self.Remove_Favorite_button.pressed.connect(self.remove_favorite)
        self.Search_button.pressed.connect(self.display_comment)

        self.show()
      
    def display_leaderboard(self):
        '''
          displays the leaderboard window
        '''
       #create sub window
        self.w = Leader_Window()
        #do stuff in window
        self.w.show()
    
    def add_Favorites(self):
       '''
          adds a comment to a list of Favorites
       '''
       self.Favorites.addItem(self.Searchbar.text())
       
    
    def select_favorite(self):
        '''
          when you select a favorite, add it to the search bar to search again
          the later funtionality will just pull up the actual comment you saved
        '''
        self.Searchbar.setText(self.Favorites.currentText())
        self.display_comment()

    def select_category(self):
        '''
          selects the category
        '''
        self.Category.setText(self.Categories.currentText())

    def remove_favorite(self):
        '''
          removes entered phrase from favorites
        '''
    
        index = self.Favorites.findText(self.Searchbar.text())
        self.Favorites.removeItem(index)

    def display_comment(self):
        '''
          display comment from webscraper
          NOTE: jeff bezos is mean to us so the scraper is not currently working
          code was made as if bezos was not mean hence html_code call
          my favorite test case is https://www.amazon.com/Monster-Energy-Zero-Ultra-Sugar/dp/B00ADYXY7E/ref=sr_1_1?crid=39MZXP8BNDI3Z&keywords=10%2Blb%2Bmonster%2Bdildo&qid=1650475481&sprefix=10%2Blb%2Bmonster%2Bdildo%2Caps%2C74&sr=8-1&th=1
        '''
        s = Scrap()
        temp = s.html_code(self.Searchbar.text())
        yeet = self.convertTuple(temp[0])
        self.Comment.setText(yeet)

    def convertTuple(self, tup):
      # initialize an empty string
        str = ''
        it = 0
        for item in tup:
          str = str + item
        return str

    def select_theme(self):
      '''
          changes themes
      '''

      if self.Themes.currentText() == "Classic Karen":
          self.central_widget.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));"
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 brown, stop:1 gold);}")
      
      if self.Themes.currentText() == "Hacker":
          self.central_widget.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(0, 255, 0, 255));"
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 black, stop:1 black);}")

      if self.Themes.currentText() == "Go Vols":
          self.central_widget.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));"
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 orange, stop:1 white);}")   
          
      if self.Themes.currentText() == "Rechot Games":
          self.central_widget.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));"
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 purple, stop:1 black);}")

      if self.Themes.currentText() == "Discord":
          self.central_widget.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 charcoal, stop:1 grey);}")              
      

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    
    window = Main_Window()
    window.show()

    sys.exit(app.exec())
