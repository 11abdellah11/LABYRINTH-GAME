from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

import pandas as pd

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt


from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import csv
from jeu import *

from view import *








app = QApplication(sys.argv)

#window and settings
window = QWidget()
window.setWindowTitle("gameeeeee labyrinthe")
window.setFixedWidth(1300)
#place window in (x,y) coordinates
window.move(333,100)
window.setStyleSheet("background-color: white ")

widgets = {
    "logo": [],
    "button": []
}



#initialliza grid layout
grid = QGridLayout()

def start_game():
    frame2()




def frame3():
    
    #clear_widgets()
    #logo 
    
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    #button widget
    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#64A314';
            border-radius: 45px;
            font-size: 30px;
            color: 'black';
            padding: 25px 0;
            margin: 100px 200px;
        }
        *:hover{
            background: '#64A314';
        }
        '''
    )
    #button callback
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    #place global widgets on the grid
    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)
    


#*********************************************
#                  FRAME 1
#*********************************************

def frame1():
    
    #clear_widgets()
    #logo 
    
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 70px;")
    widgets["logo"].append(logo)

    #button widget
    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 35px;
            font-size: 35px;
            color: 'black';
            padding: 25px 0;
            margin: 100px 200px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    #button callback
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    #place global widgets on the grid
    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)

#*********************************************
#                  FRAME 2
#*********************************************
def frame2():
    
    game.show()

    
    
    
        




game = MainWindow()
frame1()
window.setLayout(grid)
window.show()
sys.exit(app.exec()) #terminate the app