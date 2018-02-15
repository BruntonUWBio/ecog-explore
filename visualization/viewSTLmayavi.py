"""
This program reads a STL file and plots the visualization in mayavi.
First created by Junwei Huang @ Toronto, Feb 26, 2013.

Reference: http://junweihuang.info/uncategorized/3d-visualization-of-dxf-stl-file-using-mayavi-python-script/

Modified by Valentina Staneva to plot brain surface and electrode positions.

Usage: python viewSTLmayavi.py both_ascii.stl trodes.txt

Notes:
* works only with ascii .stl
* currently the code is pretty slow because it appends each point
* it should be modified to read directly an .obj file as a numpy array

"""


from numpy import *
from mayavi import mlab
import pandas as pd
import sys

STLfile = sys.argv[1]
f=open(STLfile,'r')

x=[]
y=[]
z=[]
limit = 1000000
for num,line in enumerate(f):
	#if num > limit:  # line_number starts at 0.
		#break
	strarray=line.split()
	if strarray[0]=='vertex':
		x=append(x,double(strarray[1]))
		y=append(y,double(strarray[2]))
		z=append(z,double(strarray[3]))

triangles=[(i, i+1, i+2) for i in range(0, len(x),3)]

mlab.triangular_mesh(x, y, z, triangles)
pts = pd.read_csv(sys.argv[2])

mlab.points3d(pts["x"],pts["y"],pts["z"], scale_factor = 5)
mlab.show()
