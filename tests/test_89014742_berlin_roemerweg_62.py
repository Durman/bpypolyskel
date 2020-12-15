import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((12.519026756286621, -0.26715075969696045, 0.0)),
    Vector((12.864676475524902, 11.143097877502441, 0.0)),
    Vector((5.23262882232666, 11.276667594909668, 0.0)),
    Vector((5.191960334777832, 11.710813522338867, 0.0)),
    Vector((5.110623836517334, 12.122694969177246, 0.0)),
    Vector((4.941173076629639, 12.512312889099121, 0.0)),
    Vector((4.70394229888916, 12.868535041809082, 0.0)),
    Vector((4.405709266662598, 13.157965660095215, 0.0)),
    Vector((4.053252220153809, 13.402868270874023, 0.0)),
    Vector((3.6601274013519287, 13.569847106933594, 0.0)),
    Vector((3.246668577194214, 13.647770881652832, 0.0)),
    Vector((2.8196535110473633, 13.658902168273926, 0.0)),
    Vector((2.399416923522949, 13.580978393554688, 0.0)),
    Vector((1.999514102935791, 13.436263084411621, 0.0)),
    Vector((1.6402794122695923, 13.213624000549316, 0.0)),
    Vector((1.3284908533096313, 12.924193382263184, 0.0)),
    Vector((1.0777044296264648, 12.579102516174316, 0.0)),
    Vector((0.9014760851860046, 12.189484596252441, 0.0)),
    Vector((0.7998058795928955, 11.777602195739746, 0.0)),
    Vector((0.7591378688812256, 11.354588508605957, 0.0)),
    Vector((0.3727909028530121, 11.376852035522461, 0.0)),
    Vector((0.3050108551979065, 9.562344551086426, 0.0)),
    Vector((-3.056886672973633, 9.495553970336914, 0.0)),
    Vector((-3.2466752529144287, 3.4954330921173096, 0.0)),
    Vector((0.11522646993398666, 3.473168134689331, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((12.519026756286621, -0.26715075969696045, 5.783915042877197)),
    Vector((12.864676475524902, 11.143097877502441, 5.783915042877197)),
    Vector((5.23262882232666, 11.276667594909668, 5.783915042877197)),
    Vector((5.191960334777832, 11.710813522338867, 5.783915042877197)),
    Vector((5.110623836517334, 12.122694969177246, 5.783915042877197)),
    Vector((4.941173076629639, 12.512312889099121, 5.783915042877197)),
    Vector((4.70394229888916, 12.868535041809082, 5.783915042877197)),
    Vector((4.405709266662598, 13.157965660095215, 5.783915042877197)),
    Vector((4.053252220153809, 13.402868270874023, 5.783915042877197)),
    Vector((3.6601274013519287, 13.569847106933594, 5.783915042877197)),
    Vector((3.246668577194214, 13.647770881652832, 5.783915042877197)),
    Vector((2.8196535110473633, 13.658902168273926, 5.783915042877197)),
    Vector((2.399416923522949, 13.580978393554688, 5.783915042877197)),
    Vector((1.999514102935791, 13.436263084411621, 5.783915042877197)),
    Vector((1.6402794122695923, 13.213624000549316, 5.783915042877197)),
    Vector((1.3284908533096313, 12.924193382263184, 5.783915042877197)),
    Vector((1.0777044296264648, 12.579102516174316, 5.783915042877197)),
    Vector((0.9014760851860046, 12.189484596252441, 5.783915042877197)),
    Vector((0.7998058795928955, 11.777602195739746, 5.783915042877197)),
    Vector((0.7591378688812256, 11.354588508605957, 5.783915042877197)),
    Vector((0.3727909028530121, 11.376852035522461, 5.783915042877197)),
    Vector((0.3050108551979065, 9.562344551086426, 5.783915042877197)),
    Vector((-3.056886672973633, 9.495553970336914, 5.783915042877197)),
    Vector((-3.2466752529144287, 3.4954330921173096, 5.783915042877197)),
    Vector((0.11522646993398666, 3.473168134689331, 5.783915042877197)),
    Vector((0.0, 0.0, 5.783915042877197))
]
unitVectors = [
    Vector((0.03027902916073799, 0.9995415210723877, 0.0)),
    Vector((-0.999846875667572, 0.017498483881354332, 0.0)),
    Vector((-0.09326639026403427, 0.9956412315368652, 0.0)),
    Vector((-0.19373415410518646, 0.9810540676116943, 0.0)),
    Vector((-0.3988283574581146, 0.9170255661010742, 0.0)),
    Vector((-0.5542946457862854, 0.832320511341095, 0.0)),
    Vector((-0.7176177501678467, 0.6964371204376221, 0.0)),
    Vector((-0.821216344833374, 0.5706170797348022, 0.0)),
    Vector((-0.9204145073890686, 0.39094388484954834, 0.0)),
    Vector((-0.9826995134353638, 0.18520745635032654, 0.0)),
    Vector((-0.999660313129425, 0.02605881169438362, 0.0)),
    Vector((-0.9832391738891602, -0.18232041597366333, 0.0)),
    Vector((-0.9403239488601685, -0.34028083086013794, 0.0)),
    Vector((-0.8499942421913147, -0.5267919301986694, 0.0)),
    Vector((-0.7328958511352539, -0.6803408861160278, 0.0)),
    Vector((-0.5878822803497314, -0.8089464902877808, 0.0)),
    Vector((-0.4121147394180298, -0.9111320376396179, 0.0)),
    Vector((-0.23964965343475342, -0.9708594083786011, 0.0)),
    Vector((-0.09569752961397171, -0.9954105019569397, 0.0)),
    Vector((-0.9983437061309814, 0.05753028765320778, 0.0)),
    Vector((-0.037328481674194336, -0.9993030428886414, 0.0)),
    Vector((-0.9998026490211487, -0.019863009452819824, 0.0)),
    Vector((-0.03161498159170151, -0.9995000958442688, 0.0)),
    Vector((0.9999780654907227, -0.006622581742703915, 0.0)),
    Vector((-0.033157940953969955, -0.9994500875473022, 0.0)),
    Vector((0.9997723698616028, -0.021334722638130188, 0.0))
]
holesInfo = None
firstVertIndex = 26
numPolygonVerts = 26
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