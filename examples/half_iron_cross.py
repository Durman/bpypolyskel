import mathutils 
import random
import matplotlib.pyplot as plt

def examplePoly():
    # counterclockwise order, seen from top, the polygon is on the left of this contour
    verts = [
        0,
        0,
        mathutils.Vector((300, 50, 5)),
        mathutils.Vector((250, 150, 5)),
        mathutils.Vector((350, 100, 5)),
        mathutils.Vector((350, 350, 5)),
        mathutils.Vector((50,  350, 5)),
        mathutils.Vector((50,  100, 5)),
        mathutils.Vector((150, 150, 5)),
        mathutils.Vector((100, 50, 5))
    ]

    unitVectors = None

    firstVertIndex = 2
    numPolygonVerts = 8
    holesInfo = None
    return verts, numPolygonVerts, firstVertIndex, holesInfo, unitVectors
