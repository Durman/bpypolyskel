import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-0.540529727935791, -1.179986596107483, 0.0)),
    Vector((-0.6287795305252075, -2.2486536502838135, 0.0)),
    Vector((-0.26474928855895996, -3.5622236728668213, 0.0)),
    Vector((1.4671523571014404, -5.165224552154541, 0.0)),
    Vector((3.3534910678863525, -5.3767313957214355, 0.0)),
    Vector((4.611050128936768, -4.898057460784912, 0.0)),
    Vector((5.515610218048096, -4.07429313659668, 0.0)),
    Vector((6.133358001708984, -2.7161951065063477, 0.0)),
    Vector((6.21057653427124, -1.948090672492981, 0.0)),
    Vector((5.857577323913574, -0.46754148602485657, 0.0)),
    Vector((5.096423149108887, 0.5343338251113892, 0.0)),
    Vector((4.258050441741943, 1.0909311771392822, 0.0)),
    Vector((3.044616460800171, 1.4137576818466187, 0.0)),
    Vector((1.3789023160934448, 1.1243268251419067, 0.0)),
    Vector((0.0, 0.0, 2.9586308002471924)),
    Vector((-0.540529727935791, -1.179986596107483, 2.9586308002471924)),
    Vector((-0.6287795305252075, -2.2486536502838135, 2.9586308002471924)),
    Vector((-0.26474928855895996, -3.5622236728668213, 2.9586308002471924)),
    Vector((1.4671523571014404, -5.165224552154541, 2.9586308002471924)),
    Vector((3.3534910678863525, -5.3767313957214355, 2.9586308002471924)),
    Vector((4.611050128936768, -4.898057460784912, 2.9586308002471924)),
    Vector((5.515610218048096, -4.07429313659668, 2.9586308002471924)),
    Vector((6.133358001708984, -2.7161951065063477, 2.9586308002471924)),
    Vector((6.21057653427124, -1.948090672492981, 2.9586308002471924)),
    Vector((5.857577323913574, -0.46754148602485657, 2.9586308002471924)),
    Vector((5.096423149108887, 0.5343338251113892, 2.9586308002471924)),
    Vector((4.258050441741943, 1.0909311771392822, 2.9586308002471924)),
    Vector((3.044616460800171, 1.4137576818466187, 2.9586308002471924)),
    Vector((1.3789023160934448, 1.1243268251419067, 2.9586308002471924))
]
unitVectors = [
    Vector((-0.4164653420448303, -0.9091516733169556, 0.0)),
    Vector((-0.08229918777942657, -0.9966076612472534, 0.0)),
    Vector((0.2670646905899048, -0.9636785984039307, 0.0)),
    Vector((0.7338898777961731, -0.6792684197425842, 0.0)),
    Vector((0.993772566318512, -0.11142733693122864, 0.0)),
    Vector((0.934585690498352, 0.35573819279670715, 0.0)),
    Vector((0.7393551468849182, 0.6733155846595764, 0.0)),
    Vector((0.41404205560684204, 0.9102577567100525, 0.0)),
    Vector((0.10002710670232773, 0.9949847459793091, 0.0)),
    Vector((-0.23192362487316132, 0.9727339744567871, 0.0)),
    Vector((-0.6049467325210571, 0.7962659597396851, 0.0)),
    Vector((-0.8331118226051331, 0.5531046390533447, 0.0)),
    Vector((-0.9663846492767334, 0.25710058212280273, 0.0)),
    Vector((-0.9852375388145447, -0.1711927205324173, 0.0)),
    Vector((-0.7750211358070374, -0.6319352984428406, 0.0))
]
holesInfo = None
firstVertIndex = 15
numPolygonVerts = 15
faces = []


@pytest.mark.dependency()
@pytest.mark.timeout(10)
def test_polygonize():
    global faces
    faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, None, unitVectors)


@pytest.mark.dependency(depends=["test_polygonize"])
def test_numVertsInFace():
    for face in faces:
        assert len(face) >= 3


@pytest.mark.dependency(depends=["test_polygonize"])
def test_duplication():
    for face in faces:
        assert len(face) == len(set(face))