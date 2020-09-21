import numpy
import vtk
import sys
import os

# Change working directory to allow script to be run from the ParaView shell
datapath = os.path.dirname(os.path.abspath(__file__))
os.chdir(datapath)

atoms = numpy.genfromtxt('atoms.csv', delimiter=',', skip_header=1, dtype='float');
connections = numpy.genfromtxt('connections.csv', delimiter=',', skip_header=1, dtype='int');

# Create vertices from atom positions
points = vtk.vtkPoints()
for xyz in atoms:
    points.InsertNextPoint(xyz[0], xyz[1], xyz[2])

# Create line segments from connections
cells = vtk.vtkCellArray()
for index0, index1 in connections:
    cells.InsertNextCell(2, (index0, index1))

# Create a vtkPolyData dataset from points and lines
polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.SetLines(cells)

# Write vtkPolyData dataset to file in VTK legacy format
writer = vtk.vtkPolyDataWriter()
writer.SetFileName('lines.vtk')
writer.SetInputData(polydata)
writer.Write()
