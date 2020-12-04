import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-3.8481671810150146, -9.217252731323242, 0.0)),
    Vector((0.6617410778999329, -11.042893409729004, 0.0)),
    Vector((0.13666395843029022, -12.178352355957031, 0.0)),
    Vector((6.6461873054504395, -14.939071655273438, 0.0)),
    Vector((7.156877517700195, -13.837007522583008, 0.0)),
    Vector((11.587672233581543, -15.707167625427246, 0.0)),
    Vector((15.471781730651855, -6.445376396179199, 0.0)),
    Vector((12.932709693908691, -5.376716136932373, 0.0)),
    Vector((16.687339782714844, 3.5399856567382812, 0.0)),
    Vector((18.881153106689453, 2.6383049488067627, 0.0)),
    Vector((20.794424057006836, 7.302598476409912, 0.0)),
    Vector((18.60061264038086, 8.193146705627441, 0.0)),
    Vector((21.44894027709961, 14.961381912231445, 0.0)),
    Vector((34.726890563964844, 9.35094928741455, 0.0)),
    Vector((39.48844909667969, 20.783493041992188, 0.0)),
    Vector((13.263487815856934, 31.770599365234375, 0.0)),
    Vector((9.42255973815918, 22.55333709716797, 0.0)),
    Vector((9.5736083984375, 22.497676849365234, 0.0)),
    Vector((5.545653820037842, 12.857403755187988, 0.0)),
    Vector((5.394604682922363, 12.913064002990723, 0.0)),
    Vector((0.15104928612709045, -0.06679169088602066, 0.0)),
    Vector((0.0, 7.081154551613622e-10, 0.0)),
    Vector((-3.8481671810150146, -9.217252731323242, 6.388742446899414)),
    Vector((0.6617410778999329, -11.042893409729004, 6.388742446899414)),
    Vector((0.13666395843029022, -12.178352355957031, 6.388742446899414)),
    Vector((6.6461873054504395, -14.939071655273438, 6.388742446899414)),
    Vector((7.156877517700195, -13.837007522583008, 6.388742446899414)),
    Vector((11.587672233581543, -15.707167625427246, 6.388742446899414)),
    Vector((15.471781730651855, -6.445376396179199, 6.388742446899414)),
    Vector((12.932709693908691, -5.376716136932373, 6.388742446899414)),
    Vector((16.687339782714844, 3.5399856567382812, 6.388742446899414)),
    Vector((18.881153106689453, 2.6383049488067627, 6.388742446899414)),
    Vector((20.794424057006836, 7.302598476409912, 6.388742446899414)),
    Vector((18.60061264038086, 8.193146705627441, 6.388742446899414)),
    Vector((21.44894027709961, 14.961381912231445, 6.388742446899414)),
    Vector((34.726890563964844, 9.35094928741455, 6.388742446899414)),
    Vector((39.48844909667969, 20.783493041992188, 6.388742446899414)),
    Vector((13.263487815856934, 31.770599365234375, 6.388742446899414)),
    Vector((9.42255973815918, 22.55333709716797, 6.388742446899414)),
    Vector((9.5736083984375, 22.497676849365234, 6.388742446899414)),
    Vector((5.545653820037842, 12.857403755187988, 6.388742446899414)),
    Vector((5.394604682922363, 12.913064002990723, 6.388742446899414)),
    Vector((0.15104928612709045, -0.06679169088602066, 6.388742446899414)),
    Vector((0.0, 7.081154551613622e-10, 6.388742446899414))
]
unitVectors = [
    Vector((0.9269323945045471, -0.3752283751964569, 0.0)),
    Vector((-0.41972965002059937, -0.9076491594314575, 0.0)),
    Vector((0.9206273555755615, -0.3904423713684082, 0.0)),
    Vector((0.4204457998275757, 0.9073176383972168, 0.0)),
    Vector((0.9212958216667175, -0.388862669467926, 0.0)),
    Vector((0.3867379128932953, 0.9221897125244141, 0.0)),
    Vector((-0.9216902256011963, 0.3879266381263733, 0.0)),
    Vector((0.38807713985443115, 0.9216269254684448, 0.0)),
    Vector((0.9249234199523926, -0.3801534175872803, 0.0)),
    Vector((0.3795079290866852, 0.9251884818077087, 0.0)),
    Vector((-0.926567792892456, 0.3761277198791504, 0.0)),
    Vector((0.3878886103630066, 0.9217061996459961, 0.0)),
    Vector((0.9211454391479492, -0.3892185389995575, 0.0)),
    Vector((0.3844776749610901, 0.9231342673301697, 0.0)),
    Vector((-0.9223254919052124, 0.3864138722419739, 0.0)),
    Vector((-0.38464969396591187, -0.9230626225471497, 0.0)),
    Vector((0.9383214712142944, -0.3457641005516052, 0.0)),
    Vector((-0.38552650809288025, -0.9226967692375183, 0.0)),
    Vector((-0.9383218288421631, 0.3457631468772888, 0.0)),
    Vector((-0.3745668828487396, -0.9271999001502991, 0.0)),
    Vector((-0.9145768880844116, 0.4044119417667389, 0.0)),
    Vector((-0.3852674663066864, -0.9228048920631409, 0.0))
]
holesInfo = None
firstVertIndex = 22
numPolygonVerts = 22


faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, None, unitVectors)


for face in faces:
    assert len(face) >= 3


for face in faces:
    assert len(face) == len(set(face))