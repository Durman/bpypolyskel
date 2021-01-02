import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-0.11268272250890732, 1.4582853317260742, 0.0)),
    Vector((-0.5019503235816956, 2.8609108924865723, 0.0)),
    Vector((-1.1678029298782349, 4.152216911315918, 0.0)),
    Vector((-2.069265127182007, 5.298807621002197, 0.0)),
    Vector((-3.175605058670044, 6.245023250579834, 0.0)),
    Vector((-4.456090927124023, 6.957467555999756, 0.0)),
    Vector((-5.839015960693359, 7.413877010345459, 0.0)),
    Vector((-7.283404350280762, 7.580855369567871, 0.0)),
    Vector((-8.738036155700684, 7.4695353507995605, 0.0)),
    Vector((-10.141448974609375, 7.068784236907959, 0.0)),
    Vector((-11.442421913146973, 6.411998271942139, 0.0)),
    Vector((-12.589736938476562, 5.51030969619751, 0.0)),
    Vector((-13.532173156738281, 4.397113800048828, 0.0)),
    Vector((-14.24924373626709, 3.128070831298828, 0.0)),
    Vector((-14.699973106384277, 1.747708797454834, 0.0)),
    Vector((-14.863874435424805, 0.2894233167171478, 0.0)),
    Vector((-14.751190185546875, -1.157729983329773, 0.0)),
    Vector((-14.361921310424805, -2.5603551864624023, 0.0)),
    Vector((-13.696067810058594, -3.862792491912842, 0.0)),
    Vector((-12.794605255126953, -5.009382724761963, 0.0)),
    Vector((-11.688265800476074, -5.955597400665283, 0.0)),
    Vector((-10.418024063110352, -6.668041229248047, 0.0)),
    Vector((-9.024856567382812, -7.113317966461182, 0.0)),
    Vector((-7.580469608306885, -7.291428565979004, 0.0)),
    Vector((-6.125838756561279, -7.168976306915283, 0.0)),
    Vector((-4.722427845001221, -6.77935791015625, 0.0)),
    Vector((-3.4214553833007812, -6.111440658569336, 0.0)),
    Vector((-2.2741410732269287, -5.209752559661865, 0.0)),
    Vector((-1.3317043781280518, -4.107689380645752, 0.0)),
    Vector((-0.6146328449249268, -2.827515125274658, 0.0)),
    Vector((-0.16390210390090942, -1.4471533298492432, 0.0)),
    Vector((0.0, 0.0, 11.0)),
    Vector((-0.11268272250890732, 1.4582853317260742, 11.0)),
    Vector((-0.5019503235816956, 2.8609108924865723, 11.0)),
    Vector((-1.1678029298782349, 4.152216911315918, 11.0)),
    Vector((-2.069265127182007, 5.298807621002197, 11.0)),
    Vector((-3.175605058670044, 6.245023250579834, 11.0)),
    Vector((-4.456090927124023, 6.957467555999756, 11.0)),
    Vector((-5.839015960693359, 7.413877010345459, 11.0)),
    Vector((-7.283404350280762, 7.580855369567871, 11.0)),
    Vector((-8.738036155700684, 7.4695353507995605, 11.0)),
    Vector((-10.141448974609375, 7.068784236907959, 11.0)),
    Vector((-11.442421913146973, 6.411998271942139, 11.0)),
    Vector((-12.589736938476562, 5.51030969619751, 11.0)),
    Vector((-13.532173156738281, 4.397113800048828, 11.0)),
    Vector((-14.24924373626709, 3.128070831298828, 11.0)),
    Vector((-14.699973106384277, 1.747708797454834, 11.0)),
    Vector((-14.863874435424805, 0.2894233167171478, 11.0)),
    Vector((-14.751190185546875, -1.157729983329773, 11.0)),
    Vector((-14.361921310424805, -2.5603551864624023, 11.0)),
    Vector((-13.696067810058594, -3.862792491912842, 11.0)),
    Vector((-12.794605255126953, -5.009382724761963, 11.0)),
    Vector((-11.688265800476074, -5.955597400665283, 11.0)),
    Vector((-10.418024063110352, -6.668041229248047, 11.0)),
    Vector((-9.024856567382812, -7.113317966461182, 11.0)),
    Vector((-7.580469608306885, -7.291428565979004, 11.0)),
    Vector((-6.125838756561279, -7.168976306915283, 11.0)),
    Vector((-4.722427845001221, -6.77935791015625, 11.0)),
    Vector((-3.4214553833007812, -6.111440658569336, 11.0)),
    Vector((-2.2741410732269287, -5.209752559661865, 11.0)),
    Vector((-1.3317043781280518, -4.107689380645752, 11.0)),
    Vector((-0.6146328449249268, -2.827515125274658, 11.0)),
    Vector((-0.16390210390090942, -1.4471533298492432, 11.0))
]
unitVectors = [
    Vector((-0.07704103738069534, 0.9970278739929199, 0.0)),
    Vector((-0.26742023229599, 0.9635800123214722, 0.0)),
    Vector((-0.4583016037940979, 0.8887966871261597, 0.0)),
    Vector((-0.6180629134178162, 0.786128580570221, 0.0)),
    Vector((-0.7599606513977051, 0.6499690413475037, 0.0)),
    Vector((-0.8738490343093872, 0.486197292804718, 0.0)),
    Vector((-0.9496195912361145, 0.31340479850769043, 0.0)),
    Vector((-0.9933840036392212, 0.1148400530219078, 0.0)),
    Vector((-0.9970846176147461, -0.0763048604130745, 0.0)),
    Vector((-0.9615644812583923, -0.274579256772995, 0.0)),
    Vector((-0.892691433429718, -0.4506682753562927, 0.0)),
    Vector((-0.7862429022789001, -0.6179176568984985, 0.0)),
    Vector((-0.6461424827575684, -0.7632167935371399, 0.0)),
    Vector((-0.49194568395614624, -0.8706258535385132, 0.0)),
    Vector((-0.3104011118412018, -0.9506056904792786, 0.0)),
    Vector((-0.11168994754552841, -0.9937431812286377, 0.0)),
    Vector((0.0776311531662941, -0.9969821572303772, 0.0)),
    Vector((0.2674211263656616, -0.9635797142982483, 0.0)),
    Vector((0.45519959926605225, -0.8903894424438477, 0.0)),
    Vector((0.61806321144104, -0.7861283421516418, 0.0)),
    Vector((0.7599608898162842, -0.6499688029289246, 0.0)),
    Vector((0.8721813559532166, -0.48918265104293823, 0.0)),
    Vector((0.952530562877655, -0.30444273352622986, 0.0)),
    Vector((0.9924827218055725, -0.12238527089357376, 0.0)),
    Vector((0.9964755177497864, 0.08388429135084152, 0.0)),
    Vector((0.9635565280914307, 0.2675049304962158, 0.0)),
    Vector((0.8896085619926453, 0.456723690032959, 0.0)),
    Vector((0.7862427830696106, 0.6179176568984985, 0.0)),
    Vector((0.6499208211898804, 0.7600020170211792, 0.0)),
    Vector((0.48869362473487854, 0.8724554777145386, 0.0)),
    Vector((0.3104020059108734, 0.9506053924560547, 0.0)),
    Vector((0.11253879219293594, 0.9936473369598389, 0.0))
]
holesInfo = None
firstVertIndex = 32
numPolygonVerts = 32
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