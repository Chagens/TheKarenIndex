#Will Hopkirk & Caleb Hagens

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from datetime import datetime, timedelta

class Main_UI():

    def setup_UI(self, Main_Window):
        '''
           Set up the UI
        '''

        # central_widget is a way of formatting so we can add layouts in layers 
        self.central_widget = QtWidgets.QWidget(Main_Window)
        self.central_widget.setObjectName("central_widget")

        # FUN background
        self.central_widget.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));"
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 brown, stop:1 gold);}")

        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget) 
        self.central_layout.setObjectName("central_layout")

        # pre-header layout for fun themes
        self.Theme_layout = QtWidgets.QHBoxLayout()
        self.Theme_layout.setObjectName("Theme_layout")

        self.Theme = QLabel()
        self.Theme.setText("Select theme: ")
        self.Theme_layout.addWidget(self.Theme)

        self.Themes = QtWidgets.QComboBox(self.central_widget)
        self.Themes.setStyleSheet("border-radius: -20px\n")
        self.Themes.setMinimumSize(QSize(10, 0))
        self.Themes.addItem("Classic Karen")
        self.Themes.addItem("Hacker")
        self.Themes.addItem("Go Vols")
        self.Themes.addItem("Rechot Games")
        self.Themes.addItem("Discord")
        self.Theme_layout.addWidget(self.Themes)

        self.central_layout.addLayout(self.Theme_layout)

        # Header layout to display title
        self.Header_layout = QtWidgets.QHBoxLayout()
        self.Header_layout.setObjectName("Header_layout")

        self.Title = QLabel()
        self.Title.setText("The Karen Index")
        self.Header_layout.addWidget(self.Title)

        self.Clable = QLabel()
        self.Clable.setText("Category: ")
        self.Header_layout.addWidget(self.Clable)

        self.Category = QLabel()
        self.Category.setText("- No Category -")
        self.Header_layout.addWidget(self.Category)

        self.central_layout.addLayout(self.Header_layout)

        # Button_layout_1 if we want more layouts added later we can
        self.Button_layout_1 = QtWidgets.QHBoxLayout()
        self.Button_layout_1.setObjectName("Button_layout_1")
        
        self.Searchbar = QtWidgets.QLineEdit(self.central_widget)
        self.Searchbar.setStyleSheet("background: white\n")
        self.Searchbar.setMinimumSize(QSize(0, 25))
        self.Button_layout_1.addWidget(self.Searchbar)

        self.Leaderboard_button = QtWidgets.QPushButton(self.central_widget)
        self.Leaderboard_button.setText("Leaderboard")
        self.Leaderboard_button.setStyleSheet("border-radius: -20px\n")
        self.Leaderboard_button.setMinimumSize(QSize(0, 25))
        self.Button_layout_1.addWidget(self.Leaderboard_button)

        self.Categories = QtWidgets.QComboBox(self.central_widget)
        self.Categories.setStyleSheet("border-radius: -20px\n")
        self.Categories.setMinimumSize(QSize(10, 0))
        self.Categories.addItem("Funny")
        self.Categories.addItem("Anger")
        self.Categories.addItem("Scam")
        self.Categories.addItem("Politics")
        self.Categories.addItem("Racism")
        self.Button_layout_1.addWidget(self.Categories)

        self.central_layout.addLayout(self.Button_layout_1)

        self.Button_layout_3 = QtWidgets.QHBoxLayout()
        self.Button_layout_3.setObjectName("Button_layout_3")

        self.Search_button = QtWidgets.QPushButton(self.central_widget)
        self.Search_button.setText("Search")
        self.Search_button.setStyleSheet("border-radius: -20px\n")
        self.Search_button.setMinimumSize(QSize(0, 25))
        self.Button_layout_3.addWidget(self.Search_button)

        self.central_layout.addLayout(self.Button_layout_3)

        self.Button_layout_2 = QtWidgets.QHBoxLayout()
        self.Button_layout_2.setObjectName("Button_layout_2")

        self.Favorites = QtWidgets.QComboBox(self.central_widget)
        self.Favorites.setStyleSheet("border-radius: -20px\n")
        self.Favorites.setMinimumSize(QSize(10, 0))
        self.Button_layout_2.addWidget(self.Favorites)

        self.Favorite_button = QtWidgets.QPushButton(self.central_widget)
        self.Favorite_button.setText("Favorite")
        self.Favorite_button.setStyleSheet("border-radius: -20px\n")
        self.Favorite_button.setMinimumSize(QSize(0, 25))
        self.Button_layout_2.addWidget(self.Favorite_button)

        self.Remove_Favorite_button = QtWidgets.QPushButton(self.central_widget)
        self.Remove_Favorite_button.setText("Remove Favorite")
        self.Remove_Favorite_button.setStyleSheet("border-radius: -20px\n")
        self.Remove_Favorite_button.setMinimumSize(QSize(0, 25))
        self.Button_layout_2.addWidget(self.Remove_Favorite_button)

        self.central_layout.addLayout(self.Button_layout_2)

        self.Comment_layout = QtWidgets.QHBoxLayout()
        self.Comment_layout.setObjectName("Comment_layout")

        self.Comment = QLabel()
        self.Comment.setText("")
        self.Comment_layout.addWidget(self.Comment)

        self.central_layout.addLayout(self.Comment_layout)     

        Main_Window.setCentralWidget(self.central_widget)
            
    def Resize_Text_Label(self, event):
        '''
            this section keeps the window format when resized
        '''
        default_text_size = 9
        if default_text_size < (self.rect().width() // 40):
            new_size = QFont('', self.rect().width() // 40)
        else:
            new_size = QFont('', default_text_size)
        self.setFont(new_size)
        