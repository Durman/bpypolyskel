import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-4.969722747802734, -0.17810896039009094, 0.0)),
    Vector((-4.398838996887207, -16.007741928100586, 0.0)),
    Vector((98.81645202636719, -12.311058044433594, 0.0)),
    Vector((97.19080352783203, 33.007076263427734, 0.0)),
    Vector((49.87992477416992, 31.314395904541016, 0.0)),
    Vector((50.260616302490234, 20.627729415893555, 0.0)),
    Vector((75.39456939697266, 21.529699325561523, 0.0)),
    Vector((75.25545501708984, 25.392484664916992, 0.0)),
    Vector((85.76573944091797, 25.771121978759766, 0.0)),
    Vector((86.01470184326172, 18.780261993408203, 0.0)),
    Vector((80.99375915527344, 18.602075576782227, 0.0)),
    Vector((81.41112518310547, 7.058250904083252, 0.0)),
    Vector((86.43206787109375, 7.236437797546387, 0.0)),
    Vector((86.72496795654297, -0.9900677800178528, 0.0)),
    Vector((61.68606185913086, -1.8809576034545898, 0.0)),
    Vector((61.49570083618164, 3.4512438774108887, 0.0)),
    Vector((33.046077728271484, 2.437994956970215, 0.0)),
    Vector((33.23640823364258, -2.905339479446411, 0.0)),
    Vector((0.14638368785381317, -4.096557140350342, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-4.969722747802734, -0.17810896039009094, 5.85356330871582)),
    Vector((-4.398838996887207, -16.007741928100586, 5.85356330871582)),
    Vector((98.81645202636719, -12.311058044433594, 5.85356330871582)),
    Vector((97.19080352783203, 33.007076263427734, 5.85356330871582)),
    Vector((49.87992477416992, 31.314395904541016, 5.85356330871582)),
    Vector((50.260616302490234, 20.627729415893555, 5.85356330871582)),
    Vector((75.39456939697266, 21.529699325561523, 5.85356330871582)),
    Vector((75.25545501708984, 25.392484664916992, 5.85356330871582)),
    Vector((85.76573944091797, 25.771121978759766, 5.85356330871582)),
    Vector((86.01470184326172, 18.780261993408203, 5.85356330871582)),
    Vector((80.99375915527344, 18.602075576782227, 5.85356330871582)),
    Vector((81.41112518310547, 7.058250904083252, 5.85356330871582)),
    Vector((86.43206787109375, 7.236437797546387, 5.85356330871582)),
    Vector((86.72496795654297, -0.9900677800178528, 5.85356330871582)),
    Vector((61.68606185913086, -1.8809576034545898, 5.85356330871582)),
    Vector((61.49570083618164, 3.4512438774108887, 5.85356330871582)),
    Vector((33.046077728271484, 2.437994956970215, 5.85356330871582)),
    Vector((33.23640823364258, -2.905339479446411, 5.85356330871582)),
    Vector((0.14638368785381317, -4.096557140350342, 5.85356330871582)),
    Vector((0.0, 0.0, 5.85356330871582))
]
unitVectors = [
    Vector((0.036040812730789185, -0.9993503093719482, 0.0)),
    Vector((0.9993593096733093, 0.03579232469201088, 0.0)),
    Vector((-0.035848863422870636, 0.9993572235107422, 0.0)),
    Vector((-0.9993606209754944, -0.03575494885444641, 0.0)),
    Vector((0.0356004573404789, -0.9993661046028137, 0.0)),
    Vector((0.9993566870689392, 0.035863425582647324, 0.0)),
    Vector((-0.035990674048662186, 0.9993520975112915, 0.0)),
    Vector((0.9993516802787781, 0.03600205481052399, 0.0)),
    Vector((0.035589996725320816, -0.9993664622306824, 0.0)),
    Vector((-0.999370813369751, -0.035466309636831284, 0.0)),
    Vector((0.03613131120800972, -0.9993470907211304, 0.0)),
    Vector((0.999370813369751, 0.035466402769088745, 0.0)),
    Vector((0.03558189049363136, -0.9993667602539062, 0.0)),
    Vector((-0.9993675947189331, -0.03555772081017494, 0.0)),
    Vector((-0.03567753732204437, 0.9993633031845093, 0.0)),
    Vector((-0.9993664026260376, -0.03559298440814018, 0.0)),
    Vector((0.03559760004281998, -0.9993662238121033, 0.0)),
    Vector((-0.9993526339530945, -0.035975996404886246, 0.0)),
    Vector((-0.03571055456995964, 0.9993621706962585, 0.0)),
    Vector((-0.9993584156036377, -0.03581581637263298, 0.0))
]
holesInfo = None
firstVertIndex = 20
numPolygonVerts = 20


faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, None, unitVectors)


for face in faces:
    assert len(face) >= 3


for face in faces:
    assert len(face) == len(set(face))