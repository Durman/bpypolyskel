import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-1.07854425907135, -0.45640984177589417, 0.0)),
    Vector((-2.054370164871216, -1.090930700302124, 0.0)),
    Vector((-3.19283390045166, -2.204125165939331, 0.0)),
    Vector((-4.057382106781006, -3.551090717315674, 0.0)),
    Vector((-4.562416076660156, -4.942584037780762, 0.0)),
    Vector((-4.750734329223633, -6.412001132965088, 0.0)),
    Vector((-4.921944618225098, -26.182342529296875, 0.0)),
    Vector((9.10773754119873, -26.249130249023438, 0.0)),
    Vector((9.22755241394043, -6.400865077972412, 0.0)),
    Vector((9.090592384338379, -5.031635761260986, 0.0)),
    Vector((8.722516059875488, -3.9184410572052, 0.0)),
    Vector((8.183242797851562, -2.8831703662872314, 0.0)),
    Vector((7.472772121429443, -1.9592194557189941, 0.0)),
    Vector((6.6253437995910645, -1.1577198505401611, 0.0)),
    Vector((5.658077239990234, -0.5120675563812256, 0.0)),
    Vector((4.588092803955078, -0.033394474536180496, 0.0)),
    Vector((3.458189010620117, 0.2671675682067871, 0.0)),
    Vector((2.29404616355896, 0.37848660349845886, 0.0)),
    Vector((1.1299033164978027, 0.28943076729774475, 0.0)),
    Vector((0.0, 0.0, 16.0)),
    Vector((-1.07854425907135, -0.45640984177589417, 16.0)),
    Vector((-2.054370164871216, -1.090930700302124, 16.0)),
    Vector((-3.19283390045166, -2.204125165939331, 16.0)),
    Vector((-4.057382106781006, -3.551090717315674, 16.0)),
    Vector((-4.562416076660156, -4.942584037780762, 16.0)),
    Vector((-4.750734329223633, -6.412001132965088, 16.0)),
    Vector((-4.921944618225098, -26.182342529296875, 16.0)),
    Vector((9.10773754119873, -26.249130249023438, 16.0)),
    Vector((9.22755241394043, -6.400865077972412, 16.0)),
    Vector((9.090592384338379, -5.031635761260986, 16.0)),
    Vector((8.722516059875488, -3.9184410572052, 16.0)),
    Vector((8.183242797851562, -2.8831703662872314, 16.0)),
    Vector((7.472772121429443, -1.9592194557189941, 16.0)),
    Vector((6.6253437995910645, -1.1577198505401611, 16.0)),
    Vector((5.658077239990234, -0.5120675563812256, 16.0)),
    Vector((4.588092803955078, -0.033394474536180496, 16.0)),
    Vector((3.458189010620117, 0.2671675682067871, 16.0)),
    Vector((2.29404616355896, 0.37848660349845886, 16.0)),
    Vector((1.1299033164978027, 0.28943076729774475, 16.0))
]
unitVectors = [
    Vector((-0.9209358096122742, -0.3897143304347992, 0.0)),
    Vector((-0.8383516669273376, -0.545129656791687, 0.0)),
    Vector((-0.7149973511695862, -0.6991272568702698, 0.0)),
    Vector((-0.5401570200920105, -0.8415642976760864, 0.0)),
    Vector((-0.341168075799942, -0.9400023221969604, 0.0)),
    Vector((-0.1271187961101532, -0.9918875694274902, 0.0)),
    Vector((-0.00865963101387024, -0.9999625086784363, 0.0)),
    Vector((0.9999886155128479, -0.004760404583066702, 0.0)),
    Vector((0.006036431062966585, 0.999981701374054, 0.0)),
    Vector((-0.0995304062962532, 0.9950344562530518, 0.0)),
    Vector((-0.31393277645111084, 0.9494451880455017, 0.0)),
    Vector((-0.4619814157485962, 0.8868895769119263, 0.0)),
    Vector((-0.6095701456069946, 0.7927320599555969, 0.0)),
    Vector((-0.7265205383300781, 0.6871447563171387, 0.0)),
    Vector((-0.8317295908927917, 0.555181086063385, 0.0)),
    Vector((-0.9128195643424988, 0.40836307406425476, 0.0)),
    Vector((-0.9663935303688049, 0.2570672035217285, 0.0)),
    Vector((-0.995459258556366, 0.09518897533416748, 0.0)),
    Vector((-0.9970867037773132, -0.07627619802951813, 0.0)),
    Vector((-0.9687232971191406, -0.24814364314079285, 0.0))
]
holesInfo = None
firstVertIndex = 20
numPolygonVerts = 20

bpypolyskel.debugOutputs["skeleton"] = 1


faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, None, unitVectors)


# the number of vertices in a face
for face in faces:
    assert len(face) >= 3


# duplications of vertex indices
for face in faces:
    assert len(face) == len(set(face))


# edge crossing
assert not bpypolyskel.checkEdgeCrossing(bpypolyskel.debugOutputs["skeleton"])