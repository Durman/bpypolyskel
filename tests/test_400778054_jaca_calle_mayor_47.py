import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-9.665769577026367, -5.922190189361572, 0.0)),
    Vector((-16.404773712158203, -14.048500061035156, 0.0)),
    Vector((-16.5605411529541, -14.315667152404785, 0.0)),
    Vector((-16.6671199798584, -14.649624824523926, 0.0)),
    Vector((-16.699914932250977, -15.094902992248535, 0.0)),
    Vector((-16.593338012695312, -15.651500701904297, 0.0)),
    Vector((-16.371984481811523, -16.119043350219727, 0.0)),
    Vector((-16.035856246948242, -16.464134216308594, 0.0)),
    Vector((-15.617743492126465, -16.70903778076172, 0.0)),
    Vector((-7.8785600662231445, -19.013364791870117, 0.0)),
    Vector((-7.2882771492004395, -13.859272956848145, 0.0)),
    Vector((0.6476645469665527, -12.501178741455078, 0.0)),
    Vector((-0.02459484525024891, -9.094802856445312, 0.0)),
    Vector((2.721829414367676, -8.649523735046387, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-9.665769577026367, -5.922190189361572, 11.342124938964844)),
    Vector((-16.404773712158203, -14.048500061035156, 11.342124938964844)),
    Vector((-16.5605411529541, -14.315667152404785, 11.342124938964844)),
    Vector((-16.6671199798584, -14.649624824523926, 11.342124938964844)),
    Vector((-16.699914932250977, -15.094902992248535, 11.342124938964844)),
    Vector((-16.593338012695312, -15.651500701904297, 11.342124938964844)),
    Vector((-16.371984481811523, -16.119043350219727, 11.342124938964844)),
    Vector((-16.035856246948242, -16.464134216308594, 11.342124938964844)),
    Vector((-15.617743492126465, -16.70903778076172, 11.342124938964844)),
    Vector((-7.8785600662231445, -19.013364791870117, 11.342124938964844)),
    Vector((-7.2882771492004395, -13.859272956848145, 11.342124938964844)),
    Vector((0.6476645469665527, -12.501178741455078, 11.342124938964844)),
    Vector((-0.02459484525024891, -9.094802856445312, 11.342124938964844)),
    Vector((2.721829414367676, -8.649523735046387, 11.342124938964844)),
    Vector((0.0, 0.0, 11.342124938964844))
]
unitVectors = [
    Vector((-0.6383422017097473, -0.7697527408599854, 0.0)),
    Vector((-0.5036779046058655, -0.8638914823532104, 0.0)),
    Vector((-0.3040313720703125, -0.9526621103286743, 0.0)),
    Vector((-0.07345154136419296, -0.9972987771034241, 0.0)),
    Vector((0.18806269764900208, -0.9821569919586182, 0.0)),
    Vector((0.4279063045978546, -0.9038231372833252, 0.0)),
    Vector((0.6977431178092957, -0.7163479924201965, 0.0)),
    Vector((0.8628753423690796, -0.5054168701171875, 0.0)),
    Vector((0.9584182500839233, -0.2853671908378601, 0.0)),
    Vector((0.11378326267004013, 0.993505597114563, 0.0)),
    Vector((0.9856709241867065, 0.16867992281913757, 0.0)),
    Vector((-0.19361871480941772, 0.9810768365859985, 0.0)),
    Vector((0.987110435962677, 0.1600407063961029, 0.0)),
    Vector((-0.30016860365867615, 0.9538861513137817, 0.0)),
    Vector((-0.8526794910430908, -0.5224343538284302, 0.0))
]
holesInfo = None
firstVertIndex = 15
numPolygonVerts = 15
faces = []

bpypolyskel.debugOutputs["skeleton"] = 1


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


@pytest.mark.dependency(depends=["test_polygonize"])
def test_edgeCrossing():
    assert not bpypolyskel.checkEdgeCrossing(bpypolyskel.debugOutputs["skeleton"])