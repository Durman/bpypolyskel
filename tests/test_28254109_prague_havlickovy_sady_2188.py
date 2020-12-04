import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-0.37869077920913696, 1.046403169631958, 0.0)),
    Vector((6.373434543609619, 3.317324638366699, 0.0)),
    Vector((6.587788105010986, 2.7273316383361816, 0.0)),
    Vector((7.68813419342041, 3.0946874618530273, 0.0)),
    Vector((8.002520561218262, 2.1150763034820557, 0.0)),
    Vector((11.503620147705078, 3.283937454223633, 0.0)),
    Vector((11.203523635864258, 4.263548374176025, 0.0)),
    Vector((12.28243350982666, 4.6309051513671875, 0.0)),
    Vector((12.075224876403809, 5.243161678314209, 0.0)),
    Vector((18.841629028320312, 7.480702877044678, 0.0)),
    Vector((19.163162231445312, 6.434300899505615, 0.0)),
    Vector((20.29208755493164, 6.80165958404541, 0.0)),
    Vector((20.627910614013672, 5.810917377471924, 0.0)),
    Vector((24.114715576171875, 6.9909186363220215, 0.0)),
    Vector((23.821762084960938, 7.959396839141846, 0.0)),
    Vector((24.857799530029297, 8.33788776397705, 0.0)),
    Vector((24.1861515045166, 10.408427238464355, 0.0)),
    Vector((25.143592834472656, 10.753521919250488, 0.0)),
    Vector((24.31475067138672, 13.191414833068848, 0.0)),
    Vector((23.36445426940918, 12.879715919494629, 0.0)),
    Vector((22.64993667602539, 14.961387634277344, 0.0)),
    Vector((20.94940757751465, 14.404783248901367, 0.0)),
    Vector((20.377792358398438, 16.107969284057617, 0.0)),
    Vector((21.792518615722656, 16.597780227661133, 0.0)),
    Vector((15.276141166687012, 36.54621124267578, 0.0)),
    Vector((11.317779541015625, 35.23263168334961, 0.0)),
    Vector((17.855579376220703, 15.21740436553955, 0.0)),
    Vector((18.177108764648438, 15.33985710144043, 0.0)),
    Vector((18.748722076416016, 13.62553882598877, 0.0)),
    Vector((16.983884811401367, 13.013275146484375, 0.0)),
    Vector((17.33399772644043, 11.944609642028809, 0.0)),
    Vector((10.553308486938477, 9.673674583435059, 0.0)),
    Vector((10.35324478149414, 10.263667106628418, 0.0)),
    Vector((9.23861026763916, 9.907443046569824, 0.0)),
    Vector((8.909934043884277, 10.898185729980469, 0.0)),
    Vector((5.408838748931885, 9.729326248168945, 0.0)),
    Vector((5.72322416305542, 8.71631908416748, 0.0)),
    Vector((4.665749549865723, 8.360095977783203, 0.0)),
    Vector((4.8658127784729, 7.770102500915527, 0.0)),
    Vector((-1.8863071203231812, 5.51031494140625, 0.0)),
    Vector((-2.2435617446899414, 6.567850589752197, 0.0)),
    Vector((-3.5939862728118896, 6.089177131652832, 0.0)),
    Vector((-11.63931941986084, 29.833635330200195, 0.0)),
    Vector((-11.117729187011719, 30.000614166259766, 0.0)),
    Vector((-12.025146484375, 32.683414459228516, 0.0)),
    Vector((-11.060562133789062, 33.017372131347656, 0.0)),
    Vector((-11.453537940979004, 34.19736099243164, 0.0)),
    Vector((-12.439558029174805, 33.89680099487305, 0.0)),
    Vector((-12.48957347869873, 34.0415153503418, 0.0)),
    Vector((-16.526538848876953, 32.68342971801758, 0.0)),
    Vector((-16.476524353027344, 32.549842834472656, 0.0)),
    Vector((-17.44110870361328, 32.21588897705078, 0.0)),
    Vector((-17.055278778076172, 31.03590202331543, 0.0)),
    Vector((-16.069257736206055, 31.347593307495117, 0.0)),
    Vector((-15.611978530883789, 30.000625610351562, 0.0)),
    Vector((-16.597999572753906, 29.67780113220215, 0.0)),
    Vector((-16.219314575195312, 28.486682891845703, 0.0)),
    Vector((-15.1975679397583, 28.809505462646484, 0.0)),
    Vector((-15.161842346191406, 28.687053680419922, 0.0)),
    Vector((-14.640252113342285, 28.854032516479492, 0.0)),
    Vector((-6.594930648803711, 5.0984368324279785, 0.0)),
    Vector((-7.923920154571533, 4.64202880859375, 0.0)),
    Vector((-7.21655797958374, 2.5826170444488525, 0.0)),
    Vector((-8.209728240966797, 2.2709238529205322, 0.0)),
    Vector((-7.380898952484131, -0.1892380267381668, 0.0)),
    Vector((-6.373438358306885, 0.1113232970237732, 0.0)),
    Vector((-5.687510013580322, -1.9480880498886108, 0.0)),
    Vector((-4.5943074226379395, -1.5807348489761353, 0.0)),
    Vector((-4.29421329498291, -2.5158188343048096, 0.0)),
    Vector((-0.7716721296310425, -1.3692296743392944, 0.0)),
    Vector((-1.0717666149139404, -0.37848615646362305, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-0.37869077920913696, 1.046403169631958, 2.92008900642395)),
    Vector((6.373434543609619, 3.317324638366699, 2.92008900642395)),
    Vector((6.587788105010986, 2.7273316383361816, 2.92008900642395)),
    Vector((7.68813419342041, 3.0946874618530273, 2.92008900642395)),
    Vector((8.002520561218262, 2.1150763034820557, 2.92008900642395)),
    Vector((11.503620147705078, 3.283937454223633, 2.92008900642395)),
    Vector((11.203523635864258, 4.263548374176025, 2.92008900642395)),
    Vector((12.28243350982666, 4.6309051513671875, 2.92008900642395)),
    Vector((12.075224876403809, 5.243161678314209, 2.92008900642395)),
    Vector((18.841629028320312, 7.480702877044678, 2.92008900642395)),
    Vector((19.163162231445312, 6.434300899505615, 2.92008900642395)),
    Vector((20.29208755493164, 6.80165958404541, 2.92008900642395)),
    Vector((20.627910614013672, 5.810917377471924, 2.92008900642395)),
    Vector((24.114715576171875, 6.9909186363220215, 2.92008900642395)),
    Vector((23.821762084960938, 7.959396839141846, 2.92008900642395)),
    Vector((24.857799530029297, 8.33788776397705, 2.92008900642395)),
    Vector((24.1861515045166, 10.408427238464355, 2.92008900642395)),
    Vector((25.143592834472656, 10.753521919250488, 2.92008900642395)),
    Vector((24.31475067138672, 13.191414833068848, 2.92008900642395)),
    Vector((23.36445426940918, 12.879715919494629, 2.92008900642395)),
    Vector((22.64993667602539, 14.961387634277344, 2.92008900642395)),
    Vector((20.94940757751465, 14.404783248901367, 2.92008900642395)),
    Vector((20.377792358398438, 16.107969284057617, 2.92008900642395)),
    Vector((21.792518615722656, 16.597780227661133, 2.92008900642395)),
    Vector((15.276141166687012, 36.54621124267578, 2.92008900642395)),
    Vector((11.317779541015625, 35.23263168334961, 2.92008900642395)),
    Vector((17.855579376220703, 15.21740436553955, 2.92008900642395)),
    Vector((18.177108764648438, 15.33985710144043, 2.92008900642395)),
    Vector((18.748722076416016, 13.62553882598877, 2.92008900642395)),
    Vector((16.983884811401367, 13.013275146484375, 2.92008900642395)),
    Vector((17.33399772644043, 11.944609642028809, 2.92008900642395)),
    Vector((10.553308486938477, 9.673674583435059, 2.92008900642395)),
    Vector((10.35324478149414, 10.263667106628418, 2.92008900642395)),
    Vector((9.23861026763916, 9.907443046569824, 2.92008900642395)),
    Vector((8.909934043884277, 10.898185729980469, 2.92008900642395)),
    Vector((5.408838748931885, 9.729326248168945, 2.92008900642395)),
    Vector((5.72322416305542, 8.71631908416748, 2.92008900642395)),
    Vector((4.665749549865723, 8.360095977783203, 2.92008900642395)),
    Vector((4.8658127784729, 7.770102500915527, 2.92008900642395)),
    Vector((-1.8863071203231812, 5.51031494140625, 2.92008900642395)),
    Vector((-2.2435617446899414, 6.567850589752197, 2.92008900642395)),
    Vector((-3.5939862728118896, 6.089177131652832, 2.92008900642395)),
    Vector((-11.63931941986084, 29.833635330200195, 2.92008900642395)),
    Vector((-11.117729187011719, 30.000614166259766, 2.92008900642395)),
    Vector((-12.025146484375, 32.683414459228516, 2.92008900642395)),
    Vector((-11.060562133789062, 33.017372131347656, 2.92008900642395)),
    Vector((-11.453537940979004, 34.19736099243164, 2.92008900642395)),
    Vector((-12.439558029174805, 33.89680099487305, 2.92008900642395)),
    Vector((-12.48957347869873, 34.0415153503418, 2.92008900642395)),
    Vector((-16.526538848876953, 32.68342971801758, 2.92008900642395)),
    Vector((-16.476524353027344, 32.549842834472656, 2.92008900642395)),
    Vector((-17.44110870361328, 32.21588897705078, 2.92008900642395)),
    Vector((-17.055278778076172, 31.03590202331543, 2.92008900642395)),
    Vector((-16.069257736206055, 31.347593307495117, 2.92008900642395)),
    Vector((-15.611978530883789, 30.000625610351562, 2.92008900642395)),
    Vector((-16.597999572753906, 29.67780113220215, 2.92008900642395)),
    Vector((-16.219314575195312, 28.486682891845703, 2.92008900642395)),
    Vector((-15.1975679397583, 28.809505462646484, 2.92008900642395)),
    Vector((-15.161842346191406, 28.687053680419922, 2.92008900642395)),
    Vector((-14.640252113342285, 28.854032516479492, 2.92008900642395)),
    Vector((-6.594930648803711, 5.0984368324279785, 2.92008900642395)),
    Vector((-7.923920154571533, 4.64202880859375, 2.92008900642395)),
    Vector((-7.21655797958374, 2.5826170444488525, 2.92008900642395)),
    Vector((-8.209728240966797, 2.2709238529205322, 2.92008900642395)),
    Vector((-7.380898952484131, -0.1892380267381668, 2.92008900642395)),
    Vector((-6.373438358306885, 0.1113232970237732, 2.92008900642395)),
    Vector((-5.687510013580322, -1.9480880498886108, 2.92008900642395)),
    Vector((-4.5943074226379395, -1.5807348489761353, 2.92008900642395)),
    Vector((-4.29421329498291, -2.5158188343048096, 2.92008900642395)),
    Vector((-0.7716721296310425, -1.3692296743392944, 2.92008900642395)),
    Vector((-1.0717666149139404, -0.37848615646362305, 2.92008900642395)),
    Vector((0.0, 0.0, 2.92008900642395))
]
unitVectors = [
    Vector((0.9478285908699036, 0.3187802731990814, 0.0)),
    Vector((0.3414766192436218, -0.9398902654647827, 0.0)),
    Vector((0.9485347867012024, 0.3166728913784027, 0.0)),
    Vector((0.30557864904403687, -0.9521667957305908, 0.0)),
    Vector((0.9485346078872681, 0.3166734576225281, 0.0)),
    Vector((-0.29290667176246643, 0.9561409950256348, 0.0)),
    Vector((0.946631669998169, 0.322317510843277, 0.0)),
    Vector((-0.3205730617046356, 0.9472237825393677, 0.0)),
    Vector((0.9494352340698242, 0.31396299600601196, 0.0)),
    Vector((0.293721467256546, -0.9558910727500916, 0.0)),
    Vector((0.9509206414222717, 0.3094349503517151, 0.0)),
    Vector((0.32102063298225403, -0.9470722079277039, 0.0)),
    Vector((0.9472281336784363, 0.3205600678920746, 0.0)),
    Vector((-0.2895323634147644, 0.9571682810783386, 0.0)),
    Vector((0.9392828345298767, 0.3431439995765686, 0.0)),
    Vector((-0.3085553050041199, 0.9512064456939697, 0.0)),
    Vector((0.9407570958137512, 0.3390811085700989, 0.0)),
    Vector((-0.3218883275985718, 0.9467777013778687, 0.0)),
    Vector((-0.9501921534538269, -0.31166473031044006, 0.0)),
    Vector((-0.3246501684188843, 0.9458341002464294, 0.0)),
    Vector((-0.9503859877586365, -0.3110731840133667, 0.0)),
    Vector((-0.3181740939617157, 0.9480322599411011, 0.0)),
    Vector((0.9449658393859863, 0.3271690309047699, 0.0)),
    Vector((-0.3105139136314392, 0.9505688548088074, 0.0)),
    Vector((-0.9491049647331238, -0.3149598240852356, 0.0)),
    Vector((0.31049683690071106, -0.9505743384361267, 0.0)),
    Vector((0.9345211982727051, 0.3559073805809021, 0.0)),
    Vector((0.31631436944007874, -0.9486544728279114, 0.0)),
    Vector((-0.9447610974311829, -0.32775989174842834, 0.0)),
    Vector((0.311334490776062, -0.950300395488739, 0.0)),
    Vector((-0.9482332468032837, -0.3175748288631439, 0.0)),
    Vector((-0.32113462686538696, 0.9470335245132446, 0.0)),
    Vector((-0.9525379538536072, -0.3044199049472809, 0.0)),
    Vector((-0.3148726522922516, 0.9491339921951294, 0.0)),
    Vector((-0.9485346078872681, -0.3166733682155609, 0.0)),
    Vector((0.29640257358551025, -0.9550631642341614, 0.0)),
    Vector((-0.9476752877235413, -0.3192358613014221, 0.0)),
    Vector((0.32113349437713623, -0.9470339417457581, 0.0)),
    Vector((-0.9482999444007874, -0.3173753321170807, 0.0)),
    Vector((-0.32004913687705994, 0.9474009275436401, 0.0)),
    Vector((-0.9425397515296936, -0.33409401774406433, 0.0)),
    Vector((-0.3209092319011688, 0.9471099972724915, 0.0)),
    Vector((0.9523869752883911, 0.30489158630371094, 0.0)),
    Vector((-0.32040372490882874, 0.9472810626029968, 0.0)),
    Vector((0.9449669718742371, 0.32716575264930725, 0.0)),
    Vector((-0.315971702337265, 0.9487686157226562, 0.0)),
    Vector((-0.9565476179122925, -0.2915761470794678, 0.0)),
    Vector((-0.32665571570396423, 0.9451434016227722, 0.0)),
    Vector((-0.9478042125701904, -0.3188531696796417, 0.0)),
    Vector((0.350628137588501, -0.9365148544311523, 0.0)),
    Vector((-0.9449681043624878, -0.32716241478919983, 0.0)),
    Vector((0.31078609824180603, -0.9504798054695129, 0.0)),
    Vector((0.9534948468208313, 0.30140942335128784, 0.0)),
    Vector((0.3214680254459381, -0.9469204545021057, 0.0)),
    Vector((-0.9503610730171204, -0.31114935874938965, 0.0)),
    Vector((0.3029804825782776, -0.9529967904090881, 0.0)),
    Vector((0.9535382390022278, 0.3012720048427582, 0.0)),
    Vector((0.2800757884979248, -0.959977924823761, 0.0)),
    Vector((0.9523869752883911, 0.30489158630371094, 0.0)),
    Vector((0.32077381014823914, -0.9471558332443237, 0.0)),
    Vector((-0.9457811117172241, -0.32480472326278687, 0.0)),
    Vector((0.32484951615333557, -0.9457657933235168, 0.0)),
    Vector((-0.9541162252426147, -0.2994365990161896, 0.0)),
    Vector((0.3192684054374695, -0.9476643204689026, 0.0)),
    Vector((0.9582641124725342, 0.28588423132896423, 0.0)),
    Vector((0.3160029947757721, -0.9487581253051758, 0.0)),
    Vector((0.9479125142097473, 0.318530797958374, 0.0)),
    Vector((0.3055766820907593, -0.9521674513816833, 0.0)),
    Vector((0.9508939981460571, 0.3095165491104126, 0.0)),
    Vector((-0.28989166021347046, 0.9570595026016235, 0.0)),
    Vector((0.9429307579994202, 0.33298876881599426, 0.0)),
    Vector((-0.3402986228466034, 0.9403174519538879, 0.0))
]
holesInfo = None
firstVertIndex = 72
numPolygonVerts = 72
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