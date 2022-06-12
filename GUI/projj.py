import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QGraphicsScene,QGraphicsEllipseItem,QGraphicsView,QGraphicsItem
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtOpenGL import*
from PyQt5.QtGui import QBrush,QPen
from PyQt5.QtCore import Qt,QPointF
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QVBoxLayout, QLabel
import sqlite3

from numpy import true_divide



#from ContextController import ContextConttoller
#from Context import Context
#from Cable import Cable
#from Relation import Relation
#from NodeSet import NodeSet
#from Node import Node
#from mindgrafController import mindgrafcontroller
#from ReasoningController import ReasoningController




app=QApplication(sys.argv)
widget= QStackedWidget()
contextPrev=-1
node1Prev=-1
nodeBasePrev=-1
nodeMolPrev=-1

class Main(QMainWindow):
    
     
    def __init__(self):
        super(Main,self).__init__()
        loadUi("home.ui",self)
       
      
        self.createnode.clicked.connect(self.toNode)
        self.createcontext.clicked.connect(self.toContext)
        self.createpath.clicked.connect(self.toPath)
        self.createrelation.clicked.connect(self.toRelation)
        self.drawnetwork.clicked.connect(self.toDraw)
        self.fbchainb.clicked.connect(self.toFBchain)
        self.viewcontexts.clicked.connect(self.toViewContext)
        self.pathtor.clicked.connect(self.toPathtor)
        
    def toNode(self):
        global node1Prev
        node1Prev= widget.currentIndex()
        widget.setCurrentIndex(16)
    def toContext(self):
        global contextPrev
        contextPrev=widget.currentIndex()
       
        widget.setCurrentIndex(3)    
    def toPath(self):    
        widget.setCurrentIndex(5)    
    def toRelation(self): 
        widget.setCurrentIndex(4)
    def toDraw(self):    
        widget.setCurrentIndex(6)
    def toFBchain(self):    
        widget.setCurrentIndex(9)      
    def toViewContext(self):
        widget.setCurrentIndex(17)      

    
############################################################### ATTITUDE ############################333333333333333
class Attitude(QMainWindow):
      AttArr=[]
      def __init__(self):
        super(Attitude,self).__init__()
       
        loadUi("main.ui",self)
        self.createAtt.clicked.connect(self.createAttitude)
        self.next.clicked.connect(self.toWelcome)
        
        #QPushButton.unhi
      
      def createAttitude(self):
          name=self.attitudename.text()
          self.attitudesuccess.setText("Created succesfully!")
          self.allattitudes.addItem(name)
          #ContextController.setofAttitudes.append(name)
      def toWelcome(self):  
          
          widget.setCurrentIndex(widget.currentIndex()+1) 
############################################################  NODE ###########################################################
class Node(QMainWindow):
    nodeArr=[]   # add the created nodes
    def __init__(self):
        super(Node,self).__init__()
        loadUi("createnode.ui",self)
        self.base.clicked.connect(self.toBase)
        self.molecular.clicked.connect(self.toMolecular)
        self.home.clicked.connect(self.loadHome)
        self.back.clicked.connect(self.toBack)
    def toBack(self):
        global node1Prev
        widget.setCurrentIndex(node1Prev)
    def loadHome(self):
        widget.setCurrentIndex(1)  
    def toBase(self):
        global nodeBasePrev
        nodeBasePrev=widget.currentIndex()
        widget.setCurrentIndex(13)  
    def toMolecular(self):
        global nodeMolPrev
        nodeMolPrev=widget.currentIndex()
        widget.setCurrentIndex(14)  
   

class Base(QMainWindow):
     def __init__(self):
        super(Base,self).__init__()
        loadUi("base.ui",self)
        self.createbase.clicked.connect(self.createBase)
        self.back.clicked.connect(self.toBack)
        
     def toBack(self):
        global nodeBasePrev
        widget.setCurrentIndex(nodeBasePrev)
     def createBase(self):
        baseName=self.baselabel.text()
        opclose=self.closed.isChecked()
        #Node(baseName,"emptycableset")
        
class Molecular(QMainWindow):
     str=""
     def __init__(self):
        super(Molecular,self).__init__()
        loadUi("molecular.ui",self)
        self.createmolecular.clicked.connect(self.createMolecular)
        self.addnode.clicked.connect(self.addNode)
        self.remove.clicked.connect(self.removeNode)
        self.addset.clicked.connect(self.addSet)
        self.back.clicked.connect(self.toBack)
        
     def toBack(self):
        global nodeMolPrev
        widget.setCurrentIndex(nodeMolPrev)
     def addSet(self):
         relation=self.relation.currentText()
         nodeset=[]
         mySet=self.nodeset
         for x in range (0,mySet.count()):
            nodeset.append(mySet.item(x).text())
        
        #for showing ############    
         for x in range (0,len(nodeset)-1):  

             self.str=self.str+nodeset[x]+","
         self.str=self.str+nodeset[len(nodeset)-1]   
         self.cablesets.addItem(relation+":"+self.str+"")
        
         self.str=""
        
        #adding all prop nodes in one list to make one set
   
     def createMolecular(self):
        molName= self.label.text()     
     def addNode(self):
        selected=self.nodes.selectedItems()
        row=self.nodes.row(selected[0])
        #self.proplist.takeItem(row)
        self.nodeset.addItem(selected[0].text())
     def removeNode(self):
        selected=self.nodeset.selectedItems()
        row=self.nodeset.row(selected[0])
        self.nodeset.takeItem(row)
        #self.proplist.addItem(selected[0])      
########################################################## DRAW NETWORK  #############################################
class Draw(QMainWindow):
    baseL=[]
    molecularL=[]
    relationL=[]
    
    def __init__(self):
        
        super().__init__()
        loadUi("drawnetwork.ui",self)
        bbox=["fido","dog","member","car"]
        rbox=["relation1","relation2"]
        self.basebox.addItems(bbox)
        self.relationboxx.addItems(rbox)
        self.buildnetwork.clicked.connect(self.BuildNetwork)
        self.leftwire.stateChanged.connect(self.toLeft)
        self.rightwire.stateChanged.connect(self.toRight)
        self.straightwire.stateChanged.connect(self.toStraight)
        self.reset.clicked.connect(self.resetD)
        
        #get all base nodes, molecular nodes,and relations
        myscene=GraphicsScene()
        self.scene=myscene
        myscene.setSceneRect(0,0,652,435)
        self.gview.setScene(myscene)
    
        self.existingbase.stateChanged.connect(self.existingBase)
        self.newbase.stateChanged.connect(self.newBase)
        self.newmolecular.stateChanged.connect(self.newMolecular)
        self.existingwire.stateChanged.connect(self.existingWire)
        self.newwire.stateChanged.connect(self.newWire)
        

        self.relationboxx.setCurrentIndex(-1)
        self.basebox.setCurrentIndex(-1)
        self.basebox.setCurrentText("Base Nodes")
        self.relationboxx.setCurrentText("Relation")

        self.basebox.currentIndexChanged.connect(self.updateBase)
        self.relationboxx.currentIndexChanged.connect(self.updateRelation)
        self.baselabel.textChanged.connect(self.updateBaseLabel)
        self.molecularlabel.textChanged.connect(self.updateMolecularLabel)
        self.relationlabel.textChanged.connect(self.updateRelationLabel)
        self.typelabel.textChanged.connect(self.updateType)
        self.home.clicked.connect(self.loadHome)

    def resetD(self):
        b=self.scene.baseNodes
        m=self.scene.molecularNodes
        r=self.scene.relationWires
        for x in range(0,len(b)):
            self.scene.removeItem(b[x])
        for x in range(0,len(m)):
            self.scene.removeItem(m[x])   
        for x in range(0,len(r)):
            self.scene.removeItem(r[x])     
    def loadHome(self):
       widget.setCurrentIndex(1)

    def toLeft(self):
        Line.left=self.leftwire.isChecked()
        if(self.leftwire.isChecked()==False):
            self.rightwire.setEnabled(True)
            self.straightwire.setEnabled(True)
        else:
            self.rightwire.setEnabled(False)
            self.straightwire.setEnabled(False)

    def toRight(self):
        Line.right=self.rightwire.isChecked()
        if(self.rightwire.isChecked()==False):
            self.leftwire.setEnabled(True)
            self.straightwire.setEnabled(True)
        else:
            self.leftwire.setEnabled(False)
            self.straightwire.setEnabled(False)
    def toStraight(self):
        Line.straight=self.straightwire.isChecked()  
        if(self.straightwire.isChecked()==False):
            self.rightwire.setEnabled(True)
            self.leftwire.setEnabled(True)
        else:
            self.rightwire.setEnabled(False)
            self.leftwire.setEnabled(False)  
    def updateBase(self):
        self.scene.baseBox=self.basebox.currentText()
    def updateRelation(self):
        self.scene.relationBox=self.relationboxx.currentText()    
    def updateBaseLabel(self):
        self.scene.baseLabel=self.baselabel.text()    
    def updateMolecularLabel(self):
        self.scene.molecularLabel=self.molecularlabel.text()    
    def updateRelationLabel(self):
        self.scene.relationLabel=self.relationlabel.text()   
    def updateType(self):
        self.scene.typeLabel=self.typelabel.text()    


    def existingBase(self):
        if(self.existingbase.isChecked()==False):
            
            self.scene.existingBase=False
            self.newbase.setEnabled(True)
            self.newmolecular.setEnabled(True)
            self.existingwire.setEnabled(True)
            self.newwire.setEnabled(True)
        else:
            self.scene.existingBase=True
            self.newbase.setEnabled(False)
            self.newmolecular.setEnabled(False)
            self.existingwire.setEnabled(False)
            self.newwire.setEnabled(False)
    def newBase(self):
       
        if(self.newbase.isChecked()==False):
            self.scene.newBase=False
            self.existingbase.setEnabled(True)
            self.newmolecular.setEnabled(True)
            self.existingwire.setEnabled(True)
            self.newwire.setEnabled(True)
        else:
            self.scene.newBase=True
            self.existingbase.setEnabled(False)
            self.newmolecular.setEnabled(False)
            self.existingwire.setEnabled(False)
            self.newwire.setEnabled(False)
    def newMolecular(self):
        if(self.newmolecular.isChecked()==False):
            self.scene.newMolecular=False
            self.existingbase.setEnabled(True)
            self.newbase.setEnabled(True)
            self.existingwire.setEnabled(True)
            self.newwire.setEnabled(True)
        else: 
            self.scene.newMolecular=True
            self.existingbase.setEnabled(False)
            self.newbase.setEnabled(False)
            self.existingwire.setEnabled(False)
            self.newwire.setEnabled(False)   
    def newMolecular(self):
        if(self.newmolecular.isChecked()==False):
            self.scene.newMolecular=False
            self.existingbase.setEnabled(True)
            self.newbase.setEnabled(True)
            self.existingwire.setEnabled(True)
            self.newwire.setEnabled(True)
        else: 
            self.scene.newMolecular=True
            self.existingbase.setEnabled(False)
            self.newbase.setEnabled(False)
            self.existingwire.setEnabled(False)
            self.newwire.setEnabled(False)      
    def existingWire(self):
        if(self.existingwire.isChecked()==False):
            self.scene.existingWire=False
            self.existingbase.setEnabled(True)
            self.newbase.setEnabled(True)
            self.newmolecular.setEnabled(True)
            self.newwire.setEnabled(True)
        else: 
            self.scene.existingWire=True
            self.existingbase.setEnabled(False)
            self.newbase.setEnabled(False)
            self.newmolecular.setEnabled(False)
            self.newwire.setEnabled(False)  
    def newWire(self):
        if(self.newwire.isChecked()==False):
            self.scene.newWire=False
            self.existingbase.setEnabled(True)
            self.newbase.setEnabled(True)
            self.newmolecular.setEnabled(True)
            self.existingwire.setEnabled(True)
        else: 
            self.scene.newWire=True
            self.existingbase.setEnabled(False)
            self.newbase.setEnabled(False)
            self.newmolecular.setEnabled(False)
            self.existingwire.setEnabled(False) 
    def getNode(self,name):
        m=any
    def getRelation(self,name):
        r=any                        
    def BuildNetwork(self):
        molecularDict={}
        b=self.scene.baseNodes
        m=self.scene.molecularNodes
        r=self.scene.relationWires
        t=b+m
        if(t==[]):
            self.success.setStyleSheet("color:red")
            self.success.setText("No network is drawn")
        else:

            for x in range (0,len(m)):
                relationSet={}
                print("in m")
                for y in range (0,len(r)):
                    
                    print("in r")
                    if(((r[y].source.x()>=m[x].pozx)and(r[y].source.x()<=m[x].pozx+44))and((r[y].source.y()>=m[x].pozy)and(r[y].source.y()<=m[x].pozy+44))):
                        

                        
                        for z in range (0,len(t)):
                            print("in z")
                            print(r[y].name+str(r[y].destination.x())+" "+str(r[y].destination.y()))
                            print(t[z].name+" "+str(t[z].pozx)+" "+str(t[z].pozy))
                            if(((r[y].destination.x()>=t[z].pozx)and(r[y].destination.x()<=t[z].pozx+44))and((r[y].destination.y()>=t[z].pozy)and(r[y].destination.y()<=t[z].pozy+44))):
                                if r[y].name in relationSet :
                                    relationSet[r[y].name]=relationSet[r[y].name]+[t[z].name]
                                    
                                else:
                                    relationSet[r[y].name]=[t[z].name]

                                
                                print("relation: "+r[y].name+" from: "+m[x].name+ " to: "+t[z].name)  
                            
                                print("relation source x:"+str(r[y].destination.x())+" y:"+str(r[y].destination.y()))
                                print("node position x:"+str(t[z].pozx)+ " y:"+str(t[z].pozy))

                molecularDict[m[x].name]=relationSet              

            print(molecularDict)
            self.success.setStyleSheet("color:green")
            self.success.setText("Network built successfully!")
        


        # for x in range (0,len(r)):
        #     for y in range (0,len(b)):
               
        #         if(((r[x].source.x()>=b[y].pozx-45)and(r[x].source.x()<=b[y].pozx+45))and((r[x].source.y()>=b[y].pozy-45)and(r[x].source.y()<=b[y].pozy+45))):
        #             print("relation: "+r[x].name+"from: "+b[y].name)  
        #             print("relation source x:"+str(r[x].source.x())+" y:"+str(r[x].source.y()))
        #             print("node position x:"+str(b[y].pozx)+ " y:"+str(b[y].pozy))
#node object          
class NodeEllipse(QGraphicsEllipseItem):
    isPressed=False
    pozx=0
    pozy=0
    name=""
    def __init__(self):
        pass
    def __init__(self,posx,posy,r,color,name):
        super().__init__(0, 0,  r, r)
      
        self.setPos(posx,posy)
        self.pozx=posx
        self.pozy=posy
        self.name=name
        
        self.setBrush(color)
        self.setAcceptHoverEvents(True)
        self.setFlag(self.ItemIsMovable)
        self.textItem = QGraphicsSimpleTextItem(name, self)
        rect = self.textItem.boundingRect()
        rect.moveCenter(self.boundingRect().center())
        self.textItem.setPos(rect.topLeft())
      
    def mousePressEvent(self, event):
        print("i am pressed or not")
        print(self.isPressed)
        self.isPressed=True

    def mouseMoveEvent(self, event):
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()

        orig_position = self.scenePos()

        updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
        updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()
        self.setPos(updated_cursor_x, updated_cursor_y)
        self.pozx=updated_cursor_x
        self.pozy=updated_cursor_y
        #self.setRect()
        print("Node update x:"+str( updated_cursor_x)+" y:"+str( updated_cursor_y))
    def mouseReleaseEvent(self, event):
        print("i am released")
        print('Node Release x: {0}, y: {1}'.format(self.pos().x(), self.pos().y()))   
        print('my pos pozx: {0}, pozy: {1}'.format(self.pozx, self.pozy))
        # self.pozx=self.pos().x()
        # self.pozy=self.pos().y()
        # self.setPos(self.pos().x(), self.pos().y()) 
 
class GraphicsScene(QGraphicsScene):
    existingBase=False
    newBase=False
    newMolecular=False
    existingWire=False
    newWire=False
    baseBox=""
    baseLabel=""
    molecularLabel=""
    relationBox=""
    relationLabel=""
    typeLabel=""

    #keep track of all objects added to network
    baseNodes=[]
    molecularNodes=[]
    relationWires=[]

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        
        if(self.existingBase):
            pos = event.scenePos()
            posx=pos.x()
            posy=pos.y()
            print("orig pos mouse"+str(posx)+" "+str(posy))
            radius=44
            color=QBrush(Qt.green)
            myellipse=NodeEllipse(posx,posy,radius,color,self.baseBox)
            self.baseNodes.append(myellipse)
            self.addItem(myellipse)
            print(str(posx)+" "+str(posy))
        elif(self.newBase):
            pos = event.scenePos()
            posx=pos.x()
            posy=pos.y()
            radius=44
            color=QBrush(Qt.green)
            myellipse=NodeEllipse(posx,posy,radius,color,self.baseLabel)
            self.baseNodes.append(myellipse)
            self.addItem(myellipse)
            #Node(baseLabel,"")
        elif(self.newMolecular):
            pos = event.scenePos()
            posx=pos.x()
            posy=pos.y()
            radius=44
            color=QBrush(Qt.blue)
            myellipse=NodeEllipse(posx,posy,radius,color,self.molecularLabel)
            self.molecularNodes.append(myellipse)
            self.addItem(myellipse)

        elif(self.newWire):
            pos = event.scenePos()
            posx=pos.x()
            posy=pos.y()
            color=QBrush(Qt.blue)
            p1=QPoint(int(posx),int(posy))
            p2=QPoint(int(posx+40),int(posy+40))
            myline=Line(p1,p2,self.relationLabel)
            self.relationWires.append(myline)
            self.addItem(myline)
            #Relation(selfrelationLabel,self.typeLabel)
        elif(self.existingWire):
            pos = event.scenePos()
            posx=pos.x()
            posy=pos.y()
            color=QBrush(Qt.blue)
            p1=QPoint(int(posx),int(posy))
            p2=QPoint(int(posx+40),int(posy+40))
            myline=Line(p1,p2,self.relationBox)
            self.relationWires.append(myline)
            self.addItem(myline)

    
class Line (QGraphicsLineItem):

    source=QPoint()
    destination=QPoint()
    name=""
    currentx=0
    currenty=0
    right=False
    left=False
    straight=False
    
    # node1=NodeEllipse()
    # node2=NodeEllipse()
    isPressed=False
    def __init__(self,source,destination,name, parent=None):
        super().__init__(parent)
        self.name=name
        print(self.name)
        self.source = source
        
        self.setAcceptHoverEvents(True)
        self.setAcceptHoverEvents(True)
        self.setFlag(self.ItemIsMovable)
        self.setFlag(self.ItemSendsGeometryChanges)
        self.setFlag(self.ItemIsMovable)
        self.setFlag(self.ItemSendsGeometryChanges)
        self.setCursor(QtCore.Qt.SizeAllCursor) 
        pen = QPen()  # creates a default pen
        pen.setBrush(Qt.red)
        self.setPen(pen)
        # self.setPos(self.destination.x()-3,self.destination.x()+3)
        
       
        if(self.right):

            self.setLine(self.source.x(),self.source.y(),self.source.x()+70,self.source.y()+40)
            self.destination = QPoint(self.source.x()+70,self.source.y()+40)
        elif(self.straight):
            self.setLine(self.source.x(),self.source.y(),self.source.x(),self.source.y()+60)
            self.destination = QPoint(self.source.x(),self.source.y()+60)
        elif(self.left):
            self.setLine(self.source.x(),self.source.y(),self.source.x()-70,self.source.y()+40)   
            self.destination = QPoint(self.source.x()-70,self.source.y()+40) 
        

        self.textItem = QGraphicsSimpleTextItem(self.name, self)
        rect = self.textItem.boundingRect()
        rect.moveCenter(self.boundingRect().center())
       
        
        self.textItem.setPos(rect.topLeft())
        # self.move()

        

    

    def mousePressEvent(self, event):    
        self.currentx=event.scenePos().x()
        self.currenty=event.scenePos().y()
       
        isPressed=True
  
    def mouseReleaseEvent(self, event):
      
        print("Line Realease"+str(event.scenePos().x())+" y:"+str(event.scenePos().y()))
        print("Source: x: "+str(self.source.x())+" y: "+str(self.source.y())+"Dest: x: "+ str(self.destination.x())+" y: "+str(self.destination.y()))

    def mouseMoveEvent(self, event):
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()

        orig_position = self.scenePos()
        orig_source_position=self.source
        orig_dest_position=self.destination

        updated_source_x=updated_cursor_position.x() - orig_cursor_position.x() + orig_source_position.x()
        updated_source_y= updated_cursor_position.y() - orig_cursor_position.y() + orig_source_position.y()
        updated_source=QPoint(int(updated_source_x),int(updated_source_y))
        self.source=updated_source

        updated_dest_x= updated_cursor_position.x() - orig_cursor_position.x() + orig_dest_position.x()
        updated_dest_y=updated_cursor_position.y() - orig_cursor_position.y() + orig_dest_position.y()
        updated_dest=QPoint(int(updated_dest_x),int(updated_dest_y))
        self.destination=updated_dest
       
        updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
        updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()
        self.setPos(updated_cursor_x, updated_cursor_y)


        #print("Line pos x:"+str(self.pos.)+" y:"+str(self.pos.y()))
        print("Line source x:"+str(self.source.x())+" y:"+str(self.source.y()))
        print("Line update x:"+str( updated_cursor_x)+" y:"+str( updated_cursor_y))        

#################################################   PATH  #####################################################################################
class Path(QMainWindow):
    fb=False
    def __init__(self):
        
        super(Path,self).__init__()
        
        loadUi("createpath.ui",self)
        self.fb.clicked.connect(self.tofb)
        self.andor.clicked.connect(self.toAndor)
        self.compose.clicked.connect(self.toCompose)
        self.dr.clicked.connect(self.toDr)
        self.converse.clicked.connect(self.toConverse)
        self.irreflexive.clicked.connect(self.toIrreflexive)
        self.kplus.clicked.connect(self.toKplus)
        self.kstar.clicked.connect(self.toKstar)
        self.bang.clicked.connect(self.toBang)
        self.home.clicked.connect(self.loadHome)
       



    def loadHome(self):
       widget.setCurrentIndex(1)
       
    def tofb(self):
        widget.setCurrentIndex(15)
       
    def toAndor(self):
        widget.setCurrentIndex(12)
        

    def addPath(self):
        selected=self.pathlist.selectedItems()
        row=self.pathlist.row(selected[0])
        self.pathlist.takeItem(row)
        self.currentlist.addItem(selected[0])
    def removePath(self):
        selected=self.currentlist.selectedItems()
        row=self.currentlist.row(selected[0])
        self.currentlist.takeItem(row)
        self.pathlist.addItem(selected[0])   

    def toCompose(self):
        widget.setCurrentIndex(10)
  
    def toDr(self):
         widget.setCurrentIndex(11)
  
    def toConverse(self):
        selected=self.pathlist.selectedItems()
        path=self.pathtlist.row(selected[0])
        #backend
        self.pathlabel.setText("Created succesfully!")
    def toIrreflexive(self):
        selected=self.pathlist.selectedItems()
        path=self.pathtlist.row(selected[0])
        #backend
        self.pathlabel.setText("Created succesfully!")
    def toKplus(self):
        selected=self.pathlist.selectedItems()
        path=self.pathtlist.row(selected[0])
        #backend
        self.pathlabel.setText("Created succesfully!")      
    def toKstar(self):
        selected=self.pathlist.selectedItems()
        path=self.pathtlist.row(selected[0])
        #backend
        self.pathlabel.setText("Created succesfully!")
    def toBang(self):
        
        #backend
        self.pathlabel.setText("Created succesfully!")     
class FBunit(QMainWindow):
    #MGcontroller.relations
    relations=[]
    def __init__(self):
        super(FBunit,self).__init__()
        loadUi("unitpath.ui",self)
        self.home.clicked.connect(self.loadHome)
        self.createforwardb.clicked.connect(self.toForward)
        self.createbackwardb.clicked.connect(self.toBackward)

    def loadHome(self):
        widget.setCurrentIndex(1)  
    def getRelation(self,name):
        # for x in range(0,len(self.relations)):
        #     if(name.__eq__(self.relations[x].name)):
        #         return self.relations[x]
        x=any


    def toForward(self):
        relation=self.relationlist.currentText()

    def toBackward(self):      
        relation=self.relationlist.currentText()   

class Compose(QMainWindow):
    def __init__(self):
        super(Compose,self).__init__()
        loadUi("compose.ui",self)
        self.home.clicked.connect(self.loadHome)
        
    def loadHome(self):
        widget.setCurrentIndex(1)   
    def addPath(self):
        selected=self.pathlist.selectedItems()
        row=self.pathlist.row(selected[0])
        self.pathlist.takeItem(row)
        self.currentlist.addItem(selected[0])
    def removePath(self):
        selected=self.currentlist.selectedItems()
        row=self.currentlist.row(selected[0])
        self.currentlist.takeItem(row)
        self.pathlist.addItem(selected[0])   
class DomainRange(QMainWindow):
    def __init__(self):
        super(DomainRange,self).__init__()
        loadUi("domainrange.ui",self)
        self.home.clicked.connect(self.loadHome)
       
        self.createdomain.clicked.connect(self.createDomain)
        self.createrange.clicked.connect(self.createRange)
        
    def loadHome(self):
        widget.setCurrentIndex(1)   
    def createDomain(self):
        pathset=[]
        for x in range(self.currentlist.count()-1): 
            pathset.append(self.currentlist.item(x))
        selected=self.nodelist.selectedItems()
        node=self.nodelist.row(selected[0])
    def createRange(self):
        pathset=[]
        for x in range(self.currentlist.count()-1): 
            pathset.append(self.currentlist.item(x))
        selected=self.nodelist.selectedItems()
        node=self.nodelist.row(selected[0]) 
               
class AndOr(QMainWindow):
    def __init__(self) -> None:
        super(AndOr,self).__init__() 
        loadUi("andorpath.ui",self)    
        self.addpath.clicked.connect(self.addPath)
        self.removepath.clicked.connect(self.removePath)
        self.createand.clicked.connect(self.createAnd)
        self.createor.clicked.connect(self.createOr)
        self.home.clicked.connect(self.loadHome)
        
    def loadHome(self):
        widget.setCurrentIndex(1)   

    def createAnd(self):
        mylist=[]
        for x in range(self.currentlist.count()-1):
            mylist.append(self.currentlist.item(x))
    
    def createOr(self):    
        mylist=[]
        for x in range(self.currentlist.count()-1):
            mylist.append(self.currentlist.item(x))    
    def addPath(self):
        selected=self.pathlist.selectedItems()
        row=self.pathlist.row(selected[0])
        self.pathlist.takeItem(row)
        self.currentlist.addItem(selected[0])
    def removePath(self):
        selected=self.currentlist.selectedItems()
        row=self.currentlist.row(selected[0])
        self.currentlist.takeItem(row)
        self.pathlist.addItem(selected[0])                       
############################################################### RELATION ##############################################                        
class Relation(QMainWindow):
    def __init__(self):
        super(Relation,self).__init__()
        loadUi("createrelation.ui",self)
        self.home.clicked.connect(self.loadHome)
        self.creater.clicked.connect(self.createrelation)
    def createrelation(self):
        name=self.name.text()
        type=self.type.text()
        #Relation(name,type)
    def loadHome(self):
       widget.setCurrentIndex(1)

############################################################  CONTEXT ######################################################
class Context(QMainWindow):     
    currentdict={}
    fb=False
    str=""
    #list of node objects, keep track with currentset
    listofProps=[]
    #list of attitudes type
   # listofAtt=ContextController.setofAttitudes
   
    def __init__(self):
        super(Context,self).__init__()
        loadUi("createcontext.ui",self)
        #get the attitudes from Attitude list in Context controller
        #att=ContextController.setOfAttitudes
        #get the proposition nodes to show them in a list
        prop=["p1","p2","p3"]
        self.proplist.addItems(prop)
        att={"belief","desires","emotions","assertions"}
        self.attitudes.addItems(att)
        self.attitudes.setCurrentText("Attitudes")
        self.addtocontextb.clicked.connect(self.loadAddToContext)
        proplist=self.proplist
    
        
        self.addprop.clicked.connect(self.addProp)
        self.remove.clicked.connect(self.removeProp)
        self.createcontextb.clicked.connect(self.createcontext)
        
        self.addset.clicked.connect(self.addSet)
        self.removeset.clicked.connect(self.removeSet)
        self.home.clicked.connect(self.loadHome)
        self.back.clicked.connect(self.toBack)
    def toBack(self):
        print(contextPrev)
        widget.setCurrentIndex(contextPrev)


    def loadAddToContext(self):
      widget.setCurrentIndex(7) 
    def loadHome(self):
      widget.setCurrentIndex(1)    
    def createcontext(self):
      name=self.contextname.text()
      #call context constructor Context(name,currentdict)

    def addSet(self):
        plist=[]
        attitude=self.attitudes.currentText()
        mySet=self.currentlist
        #pSet=PropositionSet()
        #adding all prop nodes in one list to make one set
        for x in range (0,mySet.count()):
            plist.append(mySet.item(x).text())
        self.currentdict[attitude]=plist
        print(self.currentdict)
        #for showing ############    
        for x in range (0,len(plist)-1):    
            self.str=self.str+plist[x]+","
        self.str=self.str+plist[len(plist)-1]   
        self.allsets.addItem(attitude+":"+self.str+"")
        
        self.str=""
        #pSet.propSet=plist    
        
    def removeSet(self):
        
        
        selected=self.allsets.selectedItems()
        row=self.allsets.row(selected[0])
        x=self.allsets.currentRow()
        i=0
        #remove from dictionary
        print(x)
        print(self.currentdict)
        for key, value in self.currentdict.items():
            if(i==x):
                print(self.currentdict[key])
                del self.currentdict[key]
                
                break
            else:
                print("else")
                i=i+1

       
        print(self.currentdict)
        #remove from UI
        self.allsets.takeItem(row)
        


    def addProp(self):
        selected=self.proplist.selectedItems()
        row=self.proplist.row(selected[0])
        #self.proplist.takeItem(row)
        self.currentlist.addItem(selected[0].text())
    def removeProp(self):
        selected=self.currentlist.selectedItems()
        row=self.currentlist.row(selected[0])
        self.currentlist.takeItem(row)
        #self.proplist.addItem(selected[0])

############################################################  ADD TO CONTEXT  ####################################################        
class addToContext(QMainWindow):
    #add all context objects
    #get the dictionary
    hyps={}
    propsObjects=[]
    #ContextController.setOfContexts
    contextObject=any
    contextList=[]
    hp={"desires":['p2','p3'],"emotions":['e1','e2'],"beliefs":['b1','b2','b3']}
    
    def __init__(self):
        super(addToContext,self).__init__()
        loadUi("addtocontext.ui",self)
         #add all prop nodes to proplist
        propsObjects=["p1","p2"] 
        self.home.clicked.connect(self.loadHome)
        #contextsList=ContextController.setOfContexts
        #self.contexts.addItems(contextsList)
       
        

        self.contexts.currentIndexChanged.connect(self.addContextDetails)
         #add the chosen context dictionary to the allsets list
        for key in self.hp:
            self.allsets.addItem(str(key)+":"+str(self.hp[key]))


        
        self.add.clicked.connect(self.addtocontext)

    def loadHome(self):
       widget.setCurrentIndex(1)
 
    def addContextDetails(self):
        context=self.contexts.currentText()
        
        hyps={}
        for x in range (0,len(self.contextList)):
            if(context==self.contextList[x].name):
                hyps=self.contextList[x].hyps
                self.contextObject=self.contextList[x]
        for key in hyps:
            self.allsets.addItem(key+": "+hyps[key])


    def addtocontext(self):
        selectedprop=self.proplist.selectedItems()
        rowP=self.proplist.row(selectedprop[0])
        selectedset=self.allsets.selectedItems()
        rowS=self.allsets.row(selectedset[0])
        
        print("row"+str(rowS))
        mystr=selectedset[0].text()
        att=mystr.rpartition(':')[0]
        self.hp[att].append(selectedprop[0].text())
        self.allsets.takeItem(rowS)
        self.allsets.insertItem(rowS,str(att)+":"+ str(self.hp[att]))

        #self.contextObject.addtoContext()
        #flag=self.contextObject.checkContradiction(rowP)
        flag=True
        if(flag):
            msg = QMessageBox()
            msg.setText("Contradiction Occured! Click OK to resolve.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.buttonClicked.connect(self.toContradiction)
    def toContradiction(self):
        widget.setCurrentIndex(8) 
class viewContext(QMainWindow):  
     def __init__(self):
        super( viewContext,self).__init__()
        loadUi("viewcontexts.ui",self)
        #x=ContextController.setOfContexts
        x=["real world","mythology"]
        self.currentcontexts.addItems(x)
        self.deletecontext.clicked.connect(self.removeC)
     #def getContext(self,name):
       #l=ContextController.setOfContexts
     # for x in range(0,len(l))   :
         #if(l[x].name==name):
           #return l[x]
     def removeC(self):
         selectedc=self.currentcontexts.selectedItems()
         selectedContext=selectedc[0].text()
         row=self.currentlist.row(selectedc[0])
         self.currentcontexts.takeItem(row)
         #c=getContext( electedContext)
         #ContextController.removeContext(c)
               
##############################################################  FORWARD BACKWARD CHAINING ################################           
class FBchain(QMainWindow):
    showC=False
    def __init__(self):
        super(FBchain,self).__init__()
        loadUi("fbchain.ui",self)
        self.home.clicked.connect(self.loadHome)
        self.fchain.clicked.connect(self.createForward)
        self.bchain.clicked.connect(self.createBackward)
        self.newnode.clicked.connect(self.toNode)
        self.newcontext.clicked.connect(self.toContext)
        
    def toNode(self):
        global node1Prev
        node1Prev=widget.currentIndex()
        widget.setCurrentIndex(2) 
    def toContext(self):
        global contextPrev
        contextPrev=widget.currentIndex()
        widget.setCurrentIndex(3) 
       
       
    
    def loadHome(self):
        widget.setCurrentIndex(1)        
    def createForward(self):
        contextT=self.context.currentText()
        attitudeT=self.attitude.currentText()
        nodeT=self.attitude.currentText()
        #node=getNode(nodeT)
        #context=getContext(contextT)
        #attitude=getAttitude(attitudeT)

        #ReasoningController.ForwardChain(node, context, attitude):

    def createBackward(self):
        contextT=self.context.currentText()
        attitudeT=self.attitude.currentText()
        nodeT=self.attitude.currentText()
        #node=getNode(nodeT)
        #context=getContext(contextT)
        #attitude=getAttitude(attitudeT)

        #ReasoningController.BackwardChain(node, context, attitude):



#################################################  CONTRADICTION ####################################   
# def chooseNode(n1,n2):
#     widget.setCurrentIndex(8)   
#     x=Contradiction.removeC(n1,n2)
#     return x
# def removeFromSupports(supports):
#     widget.setCurrentIndex(16) 
#     x=Supports.removeNodes(supports)
#     return x

class Contradiction(QMainWindow):
    def __init__(self):
        super(Contradiction,self).__init__()
        loadUi("contradiction.ui",self)
        self.remove.clicked.connect(self.removeC)
    #def getNode(self,name):

    def removeNode(self,n1,n2):
        l=[n1.name,n2.name]
        self.nodes.addItems(l)
    def removeC(self):
        selected=self.proplist.selectedItems()
        node=selected[0].text()
        nodeS=self.getNode(node)
        return nodeS
   
class Supports(QMainWindow):
     givenSupports={}
     supportD={}
     currentSupport=""
     currentNodes=[]
     def __init__(self):
        super(Supports,self).__init__()
        loadUi("supports.ui",self)
        self.remove.clicked.connect(self.removeNode)
        self.supportsbox.currentIndexChanged.connect(self.updateNodes)
        supportss={"support1":["p1","p2"],"support2":["p3","p4"]}
        self.givenSupports=supportss
        for key in supportss:
            self.supportsbox.addItem(key)

     def removeNode(self):
        selected=self.supportnodes.selectedItems()
        node=selected[0].text()
        row=self.supportnodes.row(selected[0])
        self.supportnodes.takeItem(row)
        # nodeS=self.getNode(node)
        if self.currentSupport in self.supportD :
            self.supportD[self.currentSupport]+=node
        else: 
            self.supportD[self.currentSupport]=[node]
        print(self.supportD)    

    #  def showSupports(self,supports):
    #     supports={"support1":["p1","p2"],"support2":["p3","p4"]}
    #     self.givenSupports=supports
    #     for key in supports:
    #         self.supportnodes.addItem(key)
      
     def updateNodes(self):
         self.currentSupport=self.supportsbox.currentText()
         self.currentNodes=self.givenSupports[self.currentSupport]
         n=self.givenSupports[self.currentSupport]
         self.supportnodes.clear()
         for x in range(0,len(n)):
             self.supportnodes.addItem(n[x])




       



attitude=Attitude()
main=Main()
node=Node()
context=Context()
relation=Relation()
path=Path()
draw=Draw()
addToC=addToContext()
contradiction=Contradiction()
fbchain=FBchain()
compose=Compose()
domainrange=DomainRange()
andor=AndOr()
base=Base()
molecular=Molecular()
fbunit=FBunit()
supports=Supports()
viewcontext=viewContext()


widget.addWidget(attitude)#0
widget.addWidget(main)#1
widget.addWidget(node)#2
widget.addWidget(context)#3
widget.addWidget(relation)#4
widget.addWidget(path)#5
widget.addWidget(draw)#6
widget.addWidget(addToC)#7
widget.addWidget(contradiction)#8
widget.addWidget(fbchain)#9
widget.addWidget(compose)#10
widget.addWidget(domainrange)#11
widget.addWidget(andor)#12
widget.addWidget(base)#13
widget.addWidget(molecular)#14
widget.addWidget(fbunit)#15
widget.addWidget(supports)#16
widget.addWidget(viewcontext)#17




widget.setFixedHeight(435)
widget.setFixedWidth(659)

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")    


 


