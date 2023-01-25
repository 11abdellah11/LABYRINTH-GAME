from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QImage, QPixmap, QColor
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QMainWindow

import sys
from PyQt5.QtGui import QBrush

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt


from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import csv

from jeu import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.map = Map("map.csv")
        
        self.joueurA = JoueurManuel(self.map, "A", "zxqd")
        
        
        self.joueurB = JoueurManuel(self.map, "B", "gyjb")

        self.map_view = QGraphicsView(self)
        self.map_view.setFixedSize(900, 900)
        
        
        self.map_scene = QGraphicsScene()
        self.map_view.setScene(self.map_scene)
    
        self.draw_map(self.map.map,self.joueurA,self.joueurB)
    
        self.setCentralWidget(self.map_view)
        
 

    def draw_map(self,map,joueurA,joueurB):
        
        self.map_scene.clear()
    
        for y, row in enumerate(self.map.map):
            for x, item in enumerate(row):
                
                
                if item == "1":
      
                    
                    rect = self.map_scene.addRect(x*20, y*20, 20, 20)
                    rect.setBrush(QBrush(QColor(Qt.red)))
                    
                    
                elif item == "S":
      
                    
                    rect = self.map_scene.addRect(x*20, y*20, 20, 20)
                    rect.setBrush(QBrush(QColor(Qt.black)))
                    
                    
                elif  x == self.joueurA.y and y == self.joueurA.x:
   
                
                    item = 'A'
                    
                    
                    ellipse = self.map_scene.addEllipse(x*20, y*20, 20, 20)
                    ellipse.setBrush(QBrush(QColor(Qt.green)))
                    
                elif  x == self.joueurB.y and y == self.joueurB.x:
                
                    item = 'B'

                    
                    ellipse = self.map_scene.addEllipse(x*20, y*20, 20, 20)
                    ellipse.setBrush(QBrush(QColor(Qt.blue)))
                    
                    
                    
                    
    def keyPressEvent(self, event):
        
        key = event.text()
        
        if key in self.joueurA.key_up:
            if self.joueurA.move('z'):
                
                
                self.draw_map(self.map.map,self.joueurA,self.joueurB)
                
                
                if self.joueurA.has_won():
                    print('Joueur1 a gagné! Press enter to finish')
                    #break
                elif self.joueurB.has_won():
                    print('Joueur2 a gagné! Press enter to finish')
                    #break
                
                
                self.draw_map(self.map.map,self.joueurA,self.joueurB)
        elif key in self.joueurA.key_down:
            if self.joueurA.move("x"):
                
                if self.joueurA.has_won():
                    print('Joueur1 a gagné! Press enter to finish')
                    #break
                elif self.joueurB.has_won():
                    print('Joueur2 a gagné! Press enter to finish')
                    #break
                
                
                self.draw_map(map,self.joueurA,self.joueurB)
                
        elif key in self.joueurA.key_left:
            if self.joueurA.move("q"):
                
                if self.joueurA.has_won():
                    print('Joueur1 a gagné! Press enter to finish')
                    #break
                elif self.joueurB.has_won():
                    print('Joueur2 a gagné! Press enter to finish')
                    #break
                
                self.draw_map(map,self.joueurA,self.joueurB)
                
        elif key in self.joueurA.key_right:
            
            if self.joueurA.move("d"):
                
                if self.joueurA.has_won():
                    print('Joueur1 a gagné! Press enter to finish')
                    #break
                elif self.joueurB.has_won():
                    print('Joueur2 a gagné! Press enter to finish')
                    #break
                
                self.draw_map(map,self.joueurA,self.joueurB)
                
                
        elif key in self.joueurB.key_up:
            
            
            if self.joueurB.move("j"):
                
                if self.joueurA.has_won():
                    print('Joueur1 a gagné! Press enter to finish')
                    #break
                elif self.joueurB.has_won():
                    print('Joueur2 a gagné! Press enter to finish')
                    #break
                
                self.draw_map(map,self.joueurA,self.joueurB)
        elif key in self.joueurB.key_down:
            
            if self.joueurB.move("g"):
                if self.joueurA.has_won():
                    print('Joueur1 a gagné! Press enter to finish')
                    #break
                elif self.joueurB.has_won():
                    print('Joueur2 a gagné! Press enter to finish')
                    #break
                
                self.draw_map(map,self.joueurA,self.joueurB)
        elif key in self.joueurB.key_left:
            
            if self.joueurB.move("b"):
                
                if self.joueurA.has_won():
                    print('Joueur1 a gagné! Press enter to finish')
                    #break
                elif self.joueurB.has_won():
                    print('Joueur2 a gagné! Press enter to finish')
                    #break
                self.draw_map(map,self.joueurA,self.joueurB)
                
                
        elif key in self.joueurB.key_right:
            if self.joueurB.move("y"):
                
                if self.joueurA.has_won():
                    print('Joueur1 a gagné! Press enter to finish')
                    
                    
                    #break
                elif self.joueurB.has_won():
                    print('Joueur2 a gagné! Press enter to finish')
                    
                    #break
                
                self.draw_map(map,self.joueurA,self.joueurB)
                
        else:
            super().keyPressEvent(event)
                    
                    
    