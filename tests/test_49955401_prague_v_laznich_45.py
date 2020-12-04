import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.36474287509918213, -4.107689380645752, 0.0)),
    Vector((0.6508156657218933, -4.07429313659668, 0.0)),
    Vector((0.7151821255683899, -4.497307300567627, 0.0)),
    Vector((15.45508098602295, -2.8386247158050537, 0.0)),
    Vector((14.711261749267578, 8.204266548156738, 0.0)),
    Vector((-0.3933493196964264, 7.001996040344238, 0.0)),
    Vector((-0.5506891012191772, 6.83501672744751, 0.0)),
    Vector((-0.32183146476745605, 3.9629738330841064, 0.0)),
    Vector((-3.22546648979187, 3.606752395629883, 0.0)),
    Vector((-3.304136037826538, 4.141086101531982, 0.0)),
    Vector((-11.242647171020508, 3.2839367389678955, 0.0)),
    Vector((-10.90651798248291, 0.2449139952659607, 0.0)),
    Vector((-11.113920211791992, 0.22265052795410156, 0.0)),
    Vector((-10.970887184143066, -1.346954584121704, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((0.36474287509918213, -4.107689380645752, 3.0096535682678223)),
    Vector((0.6508156657218933, -4.07429313659668, 3.0096535682678223)),
    Vector((0.7151821255683899, -4.497307300567627, 3.0096535682678223)),
    Vector((15.45508098602295, -2.8386247158050537, 3.0096535682678223)),
    Vector((14.711261749267578, 8.204266548156738, 3.0096535682678223)),
    Vector((-0.3933493196964264, 7.001996040344238, 3.0096535682678223)),
    Vector((-0.5506891012191772, 6.83501672744751, 3.0096535682678223)),
    Vector((-0.32183146476745605, 3.9629738330841064, 3.0096535682678223)),
    Vector((-3.22546648979187, 3.606752395629883, 3.0096535682678223)),
    Vector((-3.304136037826538, 4.141086101531982, 3.0096535682678223)),
    Vector((-11.242647171020508, 3.2839367389678955, 3.0096535682678223)),
    Vector((-10.90651798248291, 0.2449139952659607, 3.0096535682678223)),
    Vector((-11.113920211791992, 0.22265052795410156, 3.0096535682678223)),
    Vector((-10.970887184143066, -1.346954584121704, 3.0096535682678223)),
    Vector((0.0, 0.0, 3.0096535682678223))
]
unitVectors = [
    Vector((0.9932547211647034, 0.11595292389392853, 0.0)),
    Vector((0.15042997896671295, -0.9886206388473511, 0.0)),
    Vector((0.9937279224395752, 0.11182432621717453, 0.0)),
    Vector((-0.06720500439405441, 0.9977391958236694, 0.0)),
    Vector((-0.9968471527099609, -0.07934530079364777, 0.0)),
    Vector((-0.6857870221138, -0.7278022766113281, 0.0)),
    Vector((0.07943283766508102, -0.996840238571167, 0.0)),
    Vector((-0.9925585389137268, -0.1217682734131813, 0.0)),
    Vector((-0.14565901458263397, 0.9893348217010498, 0.0)),
    Vector((-0.9942213296890259, -0.10734962671995163, 0.0)),
    Vector((0.10993398725986481, -0.9939389228820801, 0.0)),
    Vector((-0.99428790807724, -0.10673123598098755, 0.0)),
    Vector((0.09075073152780533, -0.9958736300468445, 0.0)),
    Vector((0.9925472140312195, 0.12186034023761749, 0.0)),
    Vector((0.08844714611768723, -0.9960808753967285, 0.0))
]
holesInfo = None
firstVertIndex = 15
numPolygonVerts = 15
faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, None, unitVectors)
faces = None


@pytest.mark.timeout(10)
def test_polygonize():
    global faces
    faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, None, unitVectors)


def test_numVertsInFace():
    for face in faces:
        assert len(face) >= 3


def test_duplication():
    for face in faces:
        assert len(face) == len(set(face))