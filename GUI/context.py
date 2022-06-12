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
#from context import context
#from PropositionSet import PropositionSet
#from Proposition import Proposition
#from ContextController import ContextConttoller


# class Context(QMainWindow):     
#     currentdict={}
    
#     str=""
#     #list of node objects, keep track with currentset
#     listofProps=[]
#     #list of attitudes type
#    # listofAtt=ContextController.setofAttitudes
   
#     def __init__(self):
#         super(Context,self).__init__()
#         loadUi("createcontext.ui",self)
#         #get the attitudes from Attitude list in Context controller
#         #att=ContextController.setOfAttitudes
#         #get the proposition nodes to show them in a list
#         prop=["p1","p2","p3"]
#         self.proplist.addItems(prop)
#         att={"belief","desires","emotions","assertions"}
#         self.attitudes.addItems(att)
#         self.attitudes.setCurrentText("Attitudes")
#         proplist=self.proplist
    
        
#         self.addprop.clicked.connect(self.addProp)
#         self.remove.clicked.connect(self.removeProp)
#         self.createcontextb.clicked.connect(self.createcontext)
#         self.addtocontextb.clicked.connect(addToContext)
#         self.addset.clicked.connect(self.addSet)
#         self.removeset.clicked.connect(self.removeSet)

        
#     def createcontext(self):
#       name=self.contextname.text()
#       #call context constructor Context(name,currentdict)

#     def addSet(self):
#         plist=[]
#         attitude=self.attitudes.currentText()
#         mySet=self.currentlist
#         #pSet=PropositionSet()
#         #adding all prop nodes in one list to make one set
#         for x in range (0,mySet.count()):
#             plist.append(mySet.item(x).text())
#         self.currentdict[attitude]=plist
#         print(self.currentdict)
#         #for showing ############    
#         for x in range (0,len(plist)-1):    
#             self.str=self.str+plist[x]+","
#         self.str=self.str+plist[len(plist)-1]   
#         self.allsets.addItem(attitude+":"+self.str+"")
        
#         self.str=""
#         #pSet.propSet=plist
       
        
        
#     def removeSet(self):
        
        
#         selected=self.allsets.selectedItems()
#         row=self.allsets.row(selected[0])
#         x=self.allsets.currentRow()
#         i=0
#         #remove from dictionary
#         print(x)
#         print(self.currentdict)
#         for key, value in self.currentdict.items():
#             if(i==x):
#                 print(self.currentdict[key])
#                 del self.currentdict[key]
                
#                 break
#             else:
#                 print("else")
#                 i=i+1

       
#         print(self.currentdict)
#         #remove from UI
#         self.allsets.takeItem(row)


#     def addProp(self):
#         selected=self.proplist.selectedItems()
#         row=self.proplist.row(selected[0])
#         #self.proplist.takeItem(row)
#         self.currentlist.addItem(selected[0].text())
#     def removeProp(self):
#         selected=self.currentlist.selectedItems()
#         row=self.currentlist.row(selected[0])
#         self.currentlist.takeItem(row)
#         #self.proplist.addItem(selected[0])
# class addToContext(QMainWindow):
#     #add all context objects
#     #get the dictionary
#     hyps={}
#     contextList=[]
#     def __init__(self):
#         super(addToContext,self).__init__()
#         loadUi("addtocontext.ui",self)
#          #add all prop nodes to proplist
#         #contextsList=ContextController.setOfContexts
#         #self.contexts.addItems(contextsList)
        
#         #self.contexts.currentIndexChanged.connect(self.addContextDetails)
#          #add the chosen context dictionary to the allsets list
       
#         self.add.clicked.connect(self.addtoContext)

     
#     #def addContextDetails(self):

#     def addtocontext(self):
#         selectedprop=self.proplist.selectedItems()
#         row=self.proplist.row(selectedprop[0])
#         selectedset=self.allsets.selectedItems()
#         row=self.proplist.row(selectedprop[0])
       
       
       
   


