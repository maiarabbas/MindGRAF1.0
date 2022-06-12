import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QGraphicsScene,QGraphicsEllipseItem,QGraphicsView,QGraphicsItem
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtOpenGL import*

from PyQt5.QtGui import QBrush,QPen
from PyQt5.QtCore import Qt,QPointF
from OpenGL.GL import*
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QVBoxLayout, QLabel
import sqlite3
# from syntactic.Term import Term
# from semantic.Entity import Entity

# class Node(QMainWindow):
#     nodeArr=[]   # add the created nodes
#     def __init__(self):
#         super(Node,self).__init__()
#         loadUi("createnode.ui",self)
#         self.base.clicked.connect(self.toBase)
#         self.molecular.clicked.connect(self.toMolecular)

#         #print(self.nodebutton.isChecked())
#         # if(self.nodebutton.isChecked()):
#         #     print("checked")
#         #     self.create_scene()
#         #     self.show()

#         # self.nodebutton.clicked.connect(self.create_scene)
#         # self.create_scene()
#         # self.show()
#     def toBase(self):
#         loadUi("base.ui",self)
#         self.createbase.clicked.connect(self.createBase)
        
        
        

#     def createBase(self):
#         baseName=self.baselabel.text()
#         supported=self.supported.isChecked()
#         semantic= self.sembox.currentText()
        
#         #Node(Term(),Entity(proposition),"node1")


#     def toMolecular(self):
#         loadUi("molecular.ui",self)
#         self.createmolecular.clicked.connect(self.createMolecular)

#     def createMolecular(self):
#         molName= self.label.text() 
        
    
         
    