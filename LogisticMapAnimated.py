import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys 
import re
import ast
class Simulation(object):
    def __init__(self, x, yy, z, c, how):
        self.app = QtGui.QApplication(sys.argv)
        self.window = gl.GLViewWidget() #create a window
        self.window.setGeometry(480, 270, 800, 600) #set the geometry of the window(padding x, padding y, scale x, scale y)
        self.window.setWindowTitle("Simulation")    #set the window title
        self.window.setCameraPosition(distance=30, elevation=100) #set the camera position
        self.window.show() #show the window

        self.x, self.y, self.z = x, 0, z 
        self.c, self.yy = c, yy
        self.how = how

        self.points_list = [] #create an empty points_list

        self.point_mesh = np.array([
            [0, 0, 0],
            [2, 0, 0],
            [1, 2, 0],
            [1, 1, 1]
        ])
        self.faces = np.array([
            [0, 1, 2],
            [0, 1, 3],
            [0, 2, 3],
            [1, 2, 3]
        ])

    #Update is called once per frame
    def Update(self):
        self.x = ( (self.yy*self.x) * (self.c - self.x) )#*self.deltatime
        self.y += 0.001 #( (self.yy*self.y) * (self.c - self.x) )*self.deltatime
        self.z = ( (self.yy*self.z) * (self.c - self.z) )
        if(self.yy < 3.9999999): self.yy += 0.001
        if(self.yy >= 3.999999): self.yy = 4.0
        #here ends the algorithm 
        print(self.x, self.z, self.yy)#, self.z)
        self.newpoint = (self.x, self.y, self.z) # create a newpoint tuple
        #add the new point to the points list
        self.points_list.append(self.newpoint) #add the tuple to the points_list
        self.points = np.array(self.points_list) #convert the points list to an array of tuples
        self.draw()
        
    def draw(self):
        if self.how == "1":
            self._point_mesh = gl.GLMeshItem(vertexes = self.point_mesh, faces = self.faces, smooth=False, drawFaces=False, drawEdges=True, edgeColor=(1,1,1,1))
            self._point_mesh.scale(.001, .001, .001)
            self._point_mesh.translate(self.newpoint[0], self.newpoint[1], self.newpoint[2])
            self.window.addItem(self._point_mesh)
        elif self.how == "2":
            try: self.window.removeItem(self.drawpoints)
            except Exception: pass
            self.drawpoints = gl.GLLinePlotItem(pos=self.points, width=1, antialias=True) #make a variable to store drawing data(specify the points, set antialiasing)
            self.window.addItem(self.drawpoints) #draw the item
            sphere = gl.MeshData.sphere(rows=4, cols=8)
        
    
    #start properly
    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()
            

    #animate and update  
    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.Update)
        timer.start(10)
        self.start()

if __name__ == "__main__":
                    # x    yy  z  c  how
    sim = Simulation(0.5, 3.0, 0, 1, "1")
    sim.animation()
