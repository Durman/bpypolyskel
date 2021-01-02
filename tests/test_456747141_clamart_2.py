import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 7.081154551613622e-10, 0.0)),
    Vector((-9.891973495483398, 4.875802516937256, 0.0)),
    Vector((-10.977235794067383, 2.616018772125244, 0.0)),
    Vector((-11.497868537902832, 1.2467901706695557, 0.0)),
    Vector((-11.622529983520508, -0.3896061182022095, 0.0)),
    Vector((-11.270557403564453, -1.9926074743270874, 0.0)),
    Vector((-10.595939636230469, -3.272783041000366, 0.0)),
    Vector((-9.21737003326416, -4.608619213104248, 0.0)),
    Vector((-7.912126541137695, -5.265406131744385, 0.0)),
    Vector((-6.599549770355225, -5.532574653625488, 0.0)),
    Vector((-4.964328289031982, -5.454652786254883, 0.0)),
    Vector((-3.5784223079681396, -4.964848041534424, 0.0)),
    Vector((-2.7791433334350586, -4.4527788162231445, 0.0)),
    Vector((-1.5692256689071655, -3.217133045196533, 0.0)),
    Vector((0.0, 7.081154551613622e-10, 2.923776865005493)),
    Vector((-9.891973495483398, 4.875802516937256, 2.923776865005493)),
    Vector((-10.977235794067383, 2.616018772125244, 2.923776865005493)),
    Vector((-11.497868537902832, 1.2467901706695557, 2.923776865005493)),
    Vector((-11.622529983520508, -0.3896061182022095, 2.923776865005493)),
    Vector((-11.270557403564453, -1.9926074743270874, 2.923776865005493)),
    Vector((-10.595939636230469, -3.272783041000366, 2.923776865005493)),
    Vector((-9.21737003326416, -4.608619213104248, 2.923776865005493)),
    Vector((-7.912126541137695, -5.265406131744385, 2.923776865005493)),
    Vector((-6.599549770355225, -5.532574653625488, 2.923776865005493)),
    Vector((-4.964328289031982, -5.454652786254883, 2.923776865005493)),
    Vector((-3.5784223079681396, -4.964848041534424, 2.923776865005493)),
    Vector((-2.7791433334350586, -4.4527788162231445, 2.923776865005493)),
    Vector((-1.5692256689071655, -3.217133045196533, 2.923776865005493))
]
unitVectors = [
    Vector((-0.8969583511352539, 0.4421151876449585, 0.0)),
    Vector((-0.4329145848751068, -0.9014349579811096, 0.0)),
    Vector((-0.3554121255874634, -0.9347096681594849, 0.0)),
    Vector((-0.07596037536859512, -0.9971107840538025, 0.0)),
    Vector((0.2144620567560196, -0.9767322540283203, 0.0)),
    Vector((0.4662016034126282, -0.8846786022186279, 0.0)),
    Vector((0.7181499004364014, -0.6958884596824646, 0.0)),
    Vector((0.893284022808075, -0.44949257373809814, 0.0)),
    Vector((0.9799069762229919, -0.19945521652698517, 0.0)),
    Vector((0.998866617679596, 0.04759817197918892, 0.0)),
    Vector((0.9428490400314331, 0.3332202434539795, 0.0)),
    Vector((0.8420174717903137, 0.5394502282142639, 0.0)),
    Vector((0.699629008769989, 0.714506208896637, 0.0)),
    Vector((0.43839937448501587, 0.8987802863121033, 0.0))
]
holesInfo = None
firstVertIndex = 14
numPolygonVerts = 14
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