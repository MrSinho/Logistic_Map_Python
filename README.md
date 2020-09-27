# Logistic_Map_Python

![](Images/DotsLong.PNG)

Using this Python code you can run the Logistic Map in a 3d environment. 

## Setup
Works on ```Python 3.7.8``` or later.
- Download the ```requirements.txt``` file and from the terminal type: ```pip install -r requirements.txt```; or you can type:
```python
pip install PyQtGraph
pip install PyOpenGL
pip install numpy
pip install PyQt5
```
## Code Explanation

This simulation runs the following equation: ```x = yy*x * (c - x)```.

```python
class Simulation(object):
    def __init__(self, x, yy, z, c, how):
        self.app = QtGui.QApplication(sys.argv)
        self.window = gl.GLViewWidget() #create a window
        self.window.setGeometry(480, 270, 800, 600) #set the geometry of the window(padding x, padding y, scale x, scale y)
        self.window.setWindowTitle("Simulation")    #set the window title
        self.window.setCameraPosition(distance=30, elevation=100) #set the camera position
        self.window.show() #show the window
```
When calling the ```Simulation``` class, you have to specify the initial value of ```x```, the initial value of lambda ```yy```, the initial value of ```c``` and how should the graph be shown, if with dots or with edges.
![](Images/Edges_Long.PNG) 

