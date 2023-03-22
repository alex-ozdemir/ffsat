# testdata_211_8_16
# fs = 211
# vc = 8
# f = 1.1
# pc = 16
# tc = 25
def setting():
    return 211, 8


def data(R):
    x0, x1, x2, x3, x4, x5, x6, x7,  = R.gens()
    return [
        [
            -93*x0*x3**2 + 98*x3*x4*x5 - 7*x0**2*x6 - 50*x0*x4*x6 - 84*x4*x7**2,
            69*x0*x1*x3 + 58*x1*x2*x3 + 54*x1*x3**2 + 83*x2*x5**2 - 59*x5*x7,
            -37*x1*x2**2 + 61*x4**2*x5 + 52*x0*x2*x7 + 61*x5**2*x7 + 10*x0*x6*x7,
            91*x3*x4**2 - 64*x0*x5 + 3*x4*x5 - 81*x0*x6 + 17*x1*x6,
            43*x1*x3*x7 - 25*x3**2*x7 + 73*x3*x6*x7 - 99*x2*x6 - 68*x1 + 2,
            -35*x0*x1*x3 + 99*x1*x2*x4 + 38*x0*x1*x7 - 66*x0*x4*x7 - 64*x1*x3,
            28*x2*x3*x6 - 13*x0*x1*x7 + 17*x1*x4*x7 - 105*x2*x5*x7 - 41*x4**2,
            28*x0*x2*x3 - 100*x0*x3*x5 - 57*x3**2*x7 - 59*x1*x4 + 88*x2*x6,
            67*x0**2*x3 + 84*x1*x6**2 - 73*x3*x5*x7 + 88*x0*x7**2 - 86*x4*x6,
            -99*x1**3 - 47*x2**2*x4 + 49*x4*x5**2 + 71*x0*x5*x6 - 67*x0*x3,
            -57*x1*x2*x4 + 13*x0**2*x6 - 63*x0*x6 - 46*x3 - 57*x4,
            59*x1**3 + 75*x3*x4*x5 - 9*x0*x1 - 77*x3*x4 - 25*x0*x5,
            6*x0**2*x2 - 29*x2**2*x3 + 42*x0*x6*x7 - 9*x0*x1 - 62*x5**2,
            99*x1*x3**2 + 40*x2*x3*x6 + 85*x5*x6**2 - 39*x3**2*x7 - 103*x4*x6,
            16*x3*x5**2 - 65*x2*x6**2 - 51*x3**2*x7 + 103*x0*x3 + 38*x2*x4,
            57*x3**2*x6 + 59*x5*x6**2 - 74*x3*x4*x7 - 50*x5*x7**2 - 101*x3,
        ],
        [
            -67*x1*x4**2 - 95*x5**2*x6 - 20*x0*x3 - 60*x4**2 - 6*x7**2 - 24,
            54*x3*x4*x5 - 102*x2*x5**2 + 57*x1*x4*x6 - 96*x5**2*x7 + 74*x0*x4,
            41*x0*x3*x5 + 31*x3**2*x6 + 10*x4*x5*x6 - 4*x2*x3*x7 - 64*x0*x6*x7 + 87,
            -2*x1*x2*x4 + 77*x3*x5**2 + 101*x2**2 - 94*x7**2 + 19*x4 + 14,
            72*x1*x2*x4 - 34*x2*x4**2 + 62*x0*x5*x7 - 78*x0*x5 - 87*x6*x7 + 14,
            -66*x0*x1*x2 - 74*x0*x3*x4 + 7*x4*x5*x6 + 90*x1*x5*x7 + 58*x2*x3,
            94*x0*x1**2 + 61*x0*x2*x7 + 25*x0*x3*x7 + 56*x1*x6*x7 - 55*x2 - 87,
            -32*x0*x1*x2 - 43*x0*x2*x3 + 44*x0*x2*x4 - 74*x1*x4 + 26*x0,
            79*x2**2*x5 - 36*x2*x4*x6 + 47*x0*x2 - 34*x5*x7 + 70,
            47*x2*x3**2 - 81*x0*x4**2 - 58*x1*x2*x6 - 87*x3*x5*x6 - 20*x0*x2,
            -41*x1**3 - 95*x0**2*x3 + 6*x0*x5*x6 - 71*x3*x5*x7 + 59*x3 + 8,
            -105*x1*x3*x6 + 88*x4**2*x6 - 3*x1*x6**2 + 46*x4*x6**2 + 10*x5**2*x7 + 1,
            -68*x2**3 - 68*x0*x1*x5 + 36*x1*x6**2 + 17*x2*x5*x7 + 62*x7**2 - 210,
            -19*x0**2*x6 + 11*x4*x6**2 - 103*x2*x4*x7 - 83*x1*x7**2 + 17*x7**3 - 87,
            74*x0*x2**2 + 23*x2*x3*x5 - 81*x1*x5*x6 + 53*x3*x5*x6 - 57*x6*x7**2 + 12,
            -20*x2*x3*x4 - 97*x0*x5**2 - 69*x0*x1*x7 + 13*x3*x6*x7 - 20*x0*x7 - 8,
        ],
        [
            95*x1*x3*x6 + 90*x2*x3*x6 + 68*x1*x6*x7 + 94*x4*x6 - 6*x6**2,
            30*x0*x2*x4 - 39*x5*x7**2 - 61*x6*x7**2 - 61*x7**3 - 9,
            39*x0*x2*x5 - 2*x1*x2*x6 - 56*x1*x6**2 - 88*x3**2*x7 + 25*x1*x5,
            -25*x1**2*x5 + 9*x0*x4*x7 + 67*x1*x5 - 60*x5*x6 - 83*x4 - 98,
            13*x2**2*x4 - 45*x1**2*x5 + 63*x1*x5**2 - 32*x4**2*x7 - 27*x3*x5,
            -72*x0*x1*x3 + 98*x3*x4**2 - 10*x4*x5*x6 + 15*x1*x5*x7 - 18*x3*x5*x7,
            23*x1*x3*x4 - 87*x0*x4**2 - 81*x2*x3*x5 - 30*x1*x6**2 - 35*x1*x5*x7,
            34*x2**2*x3 + 29*x0**2*x5 - 8*x1*x3*x5 - 41*x2*x5*x6 + 102*x0*x5*x7,
            -28*x2**3 + 3*x0*x3*x4 + 25*x1*x6**2 - 22*x5*x6**2 - 24*x5**2*x7 + 87,
            -61*x1**2*x2 - 92*x1**2*x6 - 40*x2**2*x7 + 92*x2*x5*x7 - 57*x4*x6,
            -80*x0**2*x2 + 90*x0**2*x3 - 43*x1*x3*x4 + 73*x5**2 - 10*x6*x7,
            -46*x0*x1*x2 - 97*x1**2*x5 - 57*x2*x3*x7 + 70*x2*x7**2 - 54*x1*x4 - 1,
            -9*x0**2*x2 + 32*x0*x2*x4 - 72*x5*x6**2 + 105*x2*x7 - 83*x1 - 7,
            85*x0*x1*x4 - 54*x0*x3*x5 + 33*x0*x5*x7 + 81*x3*x5*x7 + 43*x6 - 54,
            -8*x4*x6**2 - 22*x1*x7**2 + 47*x2*x4 - 74*x1*x7 - x7**2 - 15,
            58*x2*x3*x4 + 39*x4**2 + 87*x0*x5 - 93*x7**2 + 5*x4 - 188,
        ],
        [
            83*x0*x3*x4 - 41*x4**3 + 42*x1*x7**2 - 3*x0*x6 + 104*x5*x6,
            -80*x2**2*x3 + 6*x3*x4**2 + 105*x1*x4 - 40*x0*x7 - 59*x1*x7,
            -50*x3*x4**2 + 16*x1*x2*x6 + 51*x1*x2*x7 - 25*x0**2 + 33*x1,
            51*x2**2*x4 + 86*x2*x4*x6 + 49*x0*x3*x7 - 39*x6 - 12,
            90*x1*x4**2 - 73*x1**2*x6 - 29*x1*x5*x6 + 47*x6**3 - 103*x6**2,
            -36*x2*x5**2 - 94*x0*x5*x6 + 17*x4*x7**2 + 99*x1*x6 - 21*x6*x7,
            -5*x0**2*x1 - 65*x1**3 - 69*x0*x1*x7 + 38*x1*x5*x7 + 81*x3*x6 - 87,
            -35*x1*x2*x5 + 64*x3**2*x6 - 30*x3*x6**2 + 54*x1*x5*x7 - 70*x2*x7**2,
            53*x0**2*x4 - 97*x5*x6**2 - 44*x5*x6*x7 - 67*x2*x7**2 + 82*x5*x6,
            16*x0*x3*x5 - 29*x0*x4*x6 + 70*x1**2*x7 + 54*x0*x4*x7 + 42*x4*x6*x7,
            68*x2*x3**2 + 34*x3**3 + 68*x2**2*x5 + 19*x1*x6**2 - 89*x0*x7 - 82,
            73*x1*x2**2 + 104*x1*x5**2 + 74*x5**2*x6 + 22*x2**2 + 22*x3**2,
            -87*x1*x3*x4 - 32*x0*x4**2 + 36*x1**2*x6 + 20*x3*x6*x7 + 72*x3*x5 - 81,
            -87*x1*x3**2 - 70*x4**3 + 95*x0*x1 - 84*x2*x6 + 6*x6 - 98,
            20*x0**2*x1 - 102*x3**2*x4 + 19*x0*x2*x5 - 71*x6**3 + 37*x1*x4*x7,
            -94*x2*x3*x4 + 91*x4**3 - 87*x3*x4*x5 - 21*x2*x5*x7 - 12*x0*x7 + 25,
        ],
        [
            -80*x0*x1**2 + 78*x0*x1*x4 + 55*x2*x4**2 - 98*x2*x4*x5 - 22*x4*x6**2,
            68*x1*x3**2 - 35*x1**2*x4 + 65*x0*x4*x5 + 49*x0*x1*x6 - 3*x2*x4,
            92*x0*x2**2 - 13*x1*x3*x4 + 30*x1*x4*x6 + 33*x3*x4*x7 + 51*x3**2,
            -14*x2*x3*x6 + 2*x0*x4*x6 + 54*x1*x2*x7 - 95*x2*x3*x7 + 28*x2*x4 + 87,
            -22*x1*x2*x4 + 78*x6**2*x7 - 29*x0*x7 + 53*x3,
            101*x1*x2*x4 - 88*x0*x4**2 + 38*x0*x1*x5 + 68*x5*x7**2 + 4*x1*x5,
            26*x3**3 + 24*x2**2*x4 + 61*x1*x3*x4 - 11*x3*x6**2 - 74*x2*x5 + 31,
            11*x3*x4*x5 + 28*x4**2*x6 - 13*x3*x4*x7 - 44*x4*x5*x7 - 67*x2*x5,
            -97*x0*x2*x6 + 39*x2*x3*x6 - 65*x0*x5*x7 + 21*x0*x3 - 26*x5**2,
            -32*x0**2*x3 + 56*x0*x4*x5 + 7*x1*x5**2 + 33*x2*x6**2 + 94*x3*x7**2,
            92*x3**2*x6 + 30*x0*x3*x7 + 85*x2*x6*x7 + 67*x3*x7 - 71*x2 + 1,
            82*x3*x4**2 + 73*x5**3 + 54*x3*x4 + 6*x0*x5 + 33*x3*x6 - 6,
            -6*x0**2*x3 - 27*x4**2*x5 + 26*x2*x5*x6 - 19*x2*x5*x7 - 102*x5**2,
            -66*x3*x4**2 - 15*x0*x3*x5 + 50*x6**2*x7 + 9*x5*x7**2 + 57*x2*x5 - 8,
            -19*x0**2*x4 + 80*x1**2*x5 + 103*x0*x2*x5 + 25*x0*x6**2 - 28*x2,
            -95*x0*x1*x3 - 70*x6*x7**2 - 44*x0**2 - 63*x3**2 + 74,
        ],
        [
            -9*x3**3 - 87*x5*x6**2 + 34*x3 + 45*x4 + 80,
            -76*x1**3 - 97*x0*x2*x3 - 55*x1*x2*x5 - 70*x2**2*x7 - 59*x3*x7,
            -58*x0*x2*x3 + 29*x2**2*x4 + 27*x4**3 + 4*x0*x3*x5 + 20*x6**3,
            -82*x0**2*x1 - 14*x2**3 - 11*x0*x2*x4 + 86*x3*x5**2 + 69*x5,
            67*x0*x5*x6 - 48*x1**2*x7 + 20*x1*x2 - 18*x4*x5 - 59*x0*x6,
            -20*x0**2*x3 + 75*x5**3 + 16*x3**2 - 25*x3*x7 + 8,
            77*x0*x1*x2 - 92*x0*x2**2 + 89*x0*x2*x3 - 100*x0*x1*x7 - 84,
            -9*x0**2*x4 - 5*x5**3 - 48*x2**2*x7 - 94*x5*x6*x7 - 64*x6 + 4,
            61*x1**3 - 87*x1*x4*x7 + 101*x1*x6*x7 - 97*x3*x6 + 92,
            -35*x3**3 - 63*x4*x5**2 - 95*x0*x7**2 - 36*x0*x3 - 75*x7**2 + 9,
            -64*x0**2*x3 + 22*x3**3 + 5*x0*x3*x4 - 89*x0*x3*x5 - 79*x3*x6**2,
            -91*x4*x5*x6 + 41*x0*x3*x7 + 27*x4*x6*x7 + 37*x1 - 25*x3 + 87,
            -31*x1*x3*x5 + 71*x0*x5*x6 - 37*x0*x6**2 + 87*x3*x6**2 - 33*x2*x4*x7,
            54*x0*x2*x6 + 44*x5*x6**2 - 52*x1*x6*x7 + 84*x3*x4 - 38*x3*x6 + 12,
            66*x0*x1*x2 - 39*x0**2*x3 + 14*x0*x3**2 + 22*x1*x2*x4 - 33*x2**2*x4,
            -76*x0**2*x7 - 55*x2**2*x7 + 8*x2*x3 + 65*x1*x5 - 88,
        ],
        [
            10*x1*x4*x5 - 79*x6**3 - 18*x0*x1*x7 + 89*x2*x4*x7 - 81*x0*x7**2,
            83*x2*x3**2 - 83*x0*x4*x5 + 43*x3**2*x7 - 86*x0*x5 + 62*x2 - 124,
            72*x1*x2**2 - 31*x1*x3**2 + 61*x1**2*x4 + 91*x0*x5*x6 + 66*x6**2,
            -49*x1*x2*x3 - 80*x0*x4*x5 + 20*x1*x3*x6 - 38*x1*x4*x6 - 46*x0*x7**2,
            72*x0**2*x7 + 28*x4*x5*x7 - 8*x4*x6*x7 - 93*x6*x7**2 + 48*x6 + 128,
            64*x1*x3*x5 + 16*x3*x4*x6 + 97*x6**2*x7 - 59*x6**2 - 65*x7,
            11*x1**2*x2 + 44*x4**2*x5 - 47*x1*x6**2 - 43*x0*x4 - 34*x7,
            63*x1*x3*x5 + 23*x2**2*x7 + 96*x7**2 + 74*x2 + 31*x5,
            103*x2*x3*x4 + 40*x0*x4*x5 + 42*x3*x5*x6 + 105*x1*x2 + 34*x0*x3,
            69*x1*x2*x6 - 86*x2*x5*x6 - 5*x6**2*x7 + 38*x6*x7**2 + 38*x4*x7 + 98,
            -98*x0*x2**2 - 84*x0*x3**2 - 42*x0*x1*x6 + 12*x0*x4*x7 - 53*x7**3 + 14,
            8*x0**2*x3 + 76*x3**3 + 96*x1**2*x5 + 91*x3**2*x6 - 43*x4*x7**2,
            -96*x0*x4*x7 + 12*x1*x4*x7 - 48*x2*x4 + 85*x2*x6 + 73*x0 + 87,
            -39*x0*x2**2 - 67*x0*x2*x5 + 31*x5*x6**2 - 39*x2*x3*x7 - 2*x1,
            -36*x0**2*x1 + 89*x4**3 + 8*x2*x4*x6 - 9*x4**2*x6 + 39*x2*x4,
            38*x2**3 + 20*x2**2*x6 + 94*x3*x4*x7 + 84*x2*x3 + 47*x3*x5 + 32,
        ],
        [
            60*x3**2*x5 + 15*x3*x4*x5 + 23*x3*x5**2 + 104*x4*x5*x6 - 24*x0*x7**2 + 87,
            28*x0*x3*x5 + 27*x0*x3*x7 - 4*x2*x5*x7 - 16*x1*x2 + 68,
            37*x1**2*x4 - 22*x6**3 - 94*x1*x3*x7 - 17*x3*x7 + 44*x5*x7 + 4,
            49*x2*x3*x4 + 58*x0*x2*x5 + 85*x4*x5*x6 - 22*x4**2*x7 - 63,
            -24*x0*x2*x6 - 45*x1*x2*x7 + 65*x0*x4 - 2*x2*x4 - 11*x2*x5,
            104*x5**2*x6 + 55*x0*x5*x7 - 44*x0*x4 - 82*x4**2 - 16*x3*x7 + 87,
            30*x2**2*x4 + 79*x3**2*x4 - 47*x0*x2*x5 + 61*x2**2*x5 + 6*x3*x6*x7,
            -4*x2*x3*x4 - 57*x0*x1*x5 - 66*x0*x3*x6 + 30*x2*x5*x7 - 89*x1**2,
            41*x0*x1**2 + 68*x0*x3*x4 - 12*x1**2*x7 - 6*x0*x4*x7 - 100*x2*x4*x7,
            -66*x4**3 - 65*x0**2 + 19*x3*x7 - 35*x7**2 + 14,
            26*x0*x4**2 - 66*x2*x4*x5 + 56*x0**2*x6 + 16*x0*x2*x7 + 84*x1*x7 - 14,
            41*x0*x1*x5 + 18*x1**2*x5 + 19*x0*x2 + 57*x1*x4 + 77*x4,
            -51*x3*x5*x6 + 104*x2*x4*x7 + 30*x3*x6*x7 + 22*x4*x7**2 - 51*x4**2,
            77*x0*x4**2 - 26*x6**3 + 8*x5**2*x7 - 60*x2**2 - 15*x3**2,
            62*x3**2*x7 - 82*x4*x7**2 - 49*x2*x3 + 30*x7**2 - 93*x5,
            56*x3**2*x5 + 85*x4*x5**2 + 44*x1**2*x6 + 104*x5*x7 + 9*x4 - 5,
        ],
        [
            -25*x3*x5**2 - 70*x0*x2*x6 - 97*x3*x6*x7 + 65*x1*x7**2 + 80*x6*x7,
            -12*x0**2*x2 - 57*x2*x3**2 + 7*x1*x2*x5 + 2*x2*x4*x6 - 27*x2**2,
            68*x1*x2**2 + 76*x4**2*x6 - 44*x3*x5*x6 + 57*x5*x6**2 + 28*x3**2 + 58,
            -55*x0**2*x1 - 17*x0*x1*x3 + 22*x0*x4*x5 + 76*x3*x4*x7 + 30*x3*x6*x7,
            -3*x1*x5**2 - 84*x1**2*x6 + 78*x0*x6*x7 - 11*x4**2 - 94,
            101*x0*x4**2 + 88*x5**2*x7 - 21*x0*x7**2 - 22*x0**2 - 3*x0,
            100*x0*x2**2 - 63*x0*x1*x3 + 80*x0*x3**2 - 96*x6*x7 - 43*x7**2 + 7,
            23*x2*x3*x5 - 22*x4*x5**2 + 79*x3**2*x6 + 26*x1*x5*x7 + 101*x2,
            2*x0**2*x4 + 51*x3*x6**2 + 71*x0*x2*x7 + 71*x3*x5*x7 + 80*x4,
            22*x1*x2**2 + 98*x2*x5*x7 + 6*x1**2 - 38*x2*x4 - 90*x3*x7 + 1,
            -2*x0**2*x5 - 38*x0*x4*x5 - 47*x0**2*x6 + 86*x3*x5*x6 - 32*x6*x7,
            -55*x1**2*x5 + 51*x1*x2*x5 + 55*x0*x3*x6 - 10*x1**2 + 54*x1*x7 + 8,
            -4*x0**2*x3 + 65*x0*x2*x5 + 69*x3**2*x7 + 37*x1*x3 - 63,
            71*x0*x1*x4 + 85*x1*x5*x6 + 49*x1**2*x7 + 88*x7**3 - 1,
            -86*x2*x4**2 + 17*x0*x1*x5 + 74*x2*x3*x5 + 8*x4*x5**2 + 11*x3*x6 - 41,
            -72*x0*x2**2 - 56*x0*x1*x3 + 10*x2*x3**2 + 71*x4**3 + 80*x1*x2*x5 + 54,
        ],
        [
            -44*x1*x3*x4 - 84*x1*x2*x5 - 11*x0*x4*x6 + 97*x4*x6 - 50*x4*x7,
            -59*x2*x3**2 + 4*x2*x4**2 - 43*x3*x5**2 - 91*x4*x5*x6 + 38*x2*x5*x7,
            -34*x2*x3*x4 - 20*x0**2*x6 + 33*x3*x4*x6 - 101*x1*x5*x6 + 25*x7**3,
            93*x5**3 + 92*x0*x5*x7 - 60*x3*x5*x7 - 56*x3*x7**2 - 3*x2 - 2,
            -21*x0*x2*x6 - 61*x1*x6**2 + 25*x2*x6 - 80*x3*x6 - 4*x6,
            33*x1*x3**2 + 31*x0*x6*x7 - 30*x7**3 + 105*x2*x7 + 48*x7,
            -39*x1**3 + 30*x0**2*x4 - 102*x3*x4**2 - 44*x3*x5**2 - x0*x6**2,
            -85*x1*x2**2 - 22*x0*x4**2 + 36*x0*x1*x6 + 36*x1**2*x7 + 12*x1**2,
            -65*x3*x5*x6 + 83*x3*x7**2 - 101*x0*x3 - 25*x1*x4 - 88*x3 + 54,
            -20*x2**2*x3 - 103*x0*x1*x6 - 6*x1*x2*x6 + 53*x0*x5*x7 - 43*x0*x6*x7,
            62*x1**2*x2 + 102*x0*x2*x4 + 100*x4*x5**2 - 87*x1 + 59,
            15*x1*x2*x6 - 89*x0*x6**2 + 94*x3*x5*x7 + 75*x0*x6*x7 - 43*x2*x6,
            85*x2**2*x4 - 57*x2*x5*x7 - 92*x3*x6*x7 - 30*x7**3 + 33*x4 + 8,
            81*x1*x4*x5 + 75*x3**2*x6 + 14*x4*x5*x6 - 11*x0*x1*x7 + 86*x3*x4*x7,
            98*x1*x2*x3 - 37*x0**2*x4 + 5*x1*x2*x7 - 97*x0*x3*x7 - 52*x3*x6,
            99*x2*x3*x4 - 45*x0**2*x5 + 100*x2*x5*x7 - 50*x0*x3 - 20*x2 - 6,
        ],
        [
            -29*x0*x2**2 + 14*x2**3 - 52*x2*x6**2 - 55*x0**2*x7 - 9*x1,
            -98*x0*x1*x5 - 77*x0*x3*x5 + 45*x2**2*x6 - 39*x2*x5 - 91*x6*x7 - 4,
            62*x1**3 - 24*x2*x3*x6 + 43*x1*x6 - 79*x4*x6 - 52*x5,
            48*x2**3 - 22*x3**2*x6 + 63*x3*x6**2 + 105*x1*x3 + 64*x0 + 54,
            -10*x2**3 + 24*x0*x1*x6 - 23*x0*x4*x6 - 29*x0*x6 - 3*x3,
            88*x0**2*x1 - 70*x0**2*x3 - 36*x2**2*x5 - 97*x1*x5**2 - 102*x2*x7**2,
            50*x4*x5*x6 - 21*x3*x4*x7 + 93*x3*x6*x7 - 4*x4*x6*x7 - 16*x0*x7**2 + 41,
            95*x1**2*x5 - 10*x2**2*x6 + 24*x4*x6**2 + 49*x0*x6*x7 + 19*x5**2,
            -69*x0*x1*x6 - 42*x2**2*x6 - 66*x1*x5*x6 + 59*x1*x2*x7 - 98*x2**2*x7,
            33*x2**2*x4 - 46*x2**2*x5 + 7*x0*x5**2 + 82*x0*x4 + 76*x0*x7,
            -77*x1*x2*x3 + 39*x3**3 - 61*x2*x4**2 + 5*x1*x2*x5 + 16*x5**2*x7 + 25,
            85*x3*x4**2 + 40*x5*x6**2 + 2*x0*x3*x7 - 94*x3*x6*x7 + 41*x6**2,
            18*x3**2*x6 - 46*x0*x5*x6 - 94*x2*x5*x6 - 6*x6**3 - 22*x5**2*x7,
            -99*x2*x4*x5 - 6*x3*x7**2 + 59*x0*x4 - 12*x2*x7 - 90*x0 + 10,
            35*x2*x3**2 - 78*x3**2*x4 - 19*x1*x3*x7 + 67*x3*x7**2 - 40*x0,
            20*x0*x3*x4 + 43*x0**2*x6 - 105*x0**2*x7 + 44*x4**2*x7 + 32*x4*x7**2 + 7,
        ],
        [
            -98*x5*x6**2 + 92*x6**2*x7 - 83*x6*x7**2 + 63*x1*x3 - 29*x1*x5 + 24,
            -37*x0**2*x1 - 93*x0*x3*x5 + x4**2*x5 + 38*x1*x4*x6 + 39*x0,
            29*x0*x2**2 - 98*x1*x2*x3 + 61*x1*x3*x5 + 74*x3*x5**2 + 30*x4*x5**2,
            55*x1*x5**2 - 97*x6**3 - 75*x1**2*x7 + 38*x5*x6*x7 - 10*x1*x2 + 87,
            -43*x2*x3*x5 + 8*x3*x5**2 - 41*x2*x3 - 79*x3*x7 + 26*x1,
            -105*x1**2*x2 + 64*x1**2*x6 - 86*x2*x3*x6 + 77*x1**2 - 32*x0*x6,
            29*x0**2*x3 - 31*x3**2*x5 - 8*x2*x3*x6 + 48*x3*x6*x7 + 93*x3*x7**2 + 41,
            -21*x0*x1*x6 - 71*x0*x2*x6 - 89*x6**3 + 12*x0**2*x7 + 80*x0*x2,
            93*x0*x2*x3 + 85*x2*x3*x4 - 83*x1**2*x6 + 95*x0*x4*x7 + 61*x1*x2,
            38*x0*x2*x4 - 22*x1**2*x5 - 56*x7**3 - 41*x1*x3 + 14,
            62*x0*x2**2 + 95*x0*x3**2 + 71*x2*x3*x4 + 34*x1**2*x6 + 84*x0*x5*x6,
            -16*x3**2*x6 - 8*x4**2*x6 + 76*x5*x7**2 + 101*x0*x1 - 92*x5,
            -34*x2**2*x7 - 48*x3*x6*x7 + 56*x7**3 - 42*x1*x6 + 19*x2*x6 + 21,
            71*x2**3 - 94*x0*x3*x5 - 20*x1*x3*x5 + 85*x2*x4*x6 + 13*x0*x2,
            -90*x0*x2*x4 - 77*x0*x5*x6 - 81*x0*x3*x7 + 98*x0*x5 + 19*x5*x7 + 41,
            26*x2*x4*x5 - 61*x0*x2*x6 + 66*x5**2*x6 - 101*x0*x2*x7 - 43*x4*x7**2,
        ],
        [
            16*x1*x2**2 + 37*x1**2*x3 - 14*x2**2*x6 - 80*x0*x6**2 + 5*x0**2,
            82*x0**2*x2 + 74*x1**2*x2 - 24*x2**2*x3 - 14*x1**2*x7 - 44*x1*x2 + 87,
            -92*x2*x4**2 + 49*x3*x4*x5 - 27*x1*x5*x6 + 11*x0*x3*x7 - 15*x3*x7**2,
            -71*x0*x4**2 - 40*x3*x4*x5 - 79*x3**2*x7 - 65*x3*x7**2 - 64*x5*x7,
            87*x2*x4**2 + 48*x1*x4*x5 - 33*x1*x3*x6 + 46*x4*x6 + 12,
            29*x2**2*x4 + 32*x0*x1*x6 - 97*x0*x4*x7 - 58*x0*x5*x7 + 9*x4*x5*x7,
            -61*x1*x3**2 - 61*x2*x3**2 + 85*x0*x6**2 - 78*x3*x5 - 81*x5**2,
            101*x1**2*x3 + 16*x0*x3*x4 - 30*x2*x3*x4 - 54*x2**2*x5 - 57*x2*x4*x6 + 21,
            -60*x3*x5**2 - 105*x2*x6**2 - 99*x4*x5 + 37*x2*x7 - 95*x7**2,
            -2*x0*x1*x6 - 62*x2*x5*x6 + 38*x4**2*x7 - 58*x4*x6*x7 + 85*x6*x7,
            -63*x1**2*x2 - 56*x0*x1*x5 + 36*x5**2*x6 + 79*x0*x1*x7 + 103*x3*x5*x7,
            -94*x1*x3**2 + 65*x6**3 - 82*x0*x4*x7 - 91*x0*x7**2 + 86*x0*x5 + 2,
            -33*x3**3 + 20*x2**2*x4 + 94*x2**2*x5 + 46*x0*x3*x7 - 12*x3*x5,
            16*x1*x3*x4 - 71*x0*x1*x6 - 38*x2*x6*x7 - 60*x0*x7**2 - 8*x1*x7**2,
            86*x3*x4*x6 - 20*x1*x5*x6 + 96*x4*x5*x7 - 17*x5*x6 + 77*x2*x7,
            10*x2*x3*x5 - 13*x4**2*x5 - 68*x2*x7**2 - 22*x0*x7 - 99*x7 + 87,
        ],
        [
            -8*x3**2*x4 - 43*x2**2*x5 - 73*x1**2*x6 - 39*x3**2*x7 + 3*x5**2,
            -25*x1*x2*x3 + 83*x2*x5*x6 - 84*x4*x6**2 - 12*x0**2*x7 - 43*x2*x3,
            -11*x0*x3**2 - 75*x3*x4**2 - 25*x1*x6**2 - 43*x1**2 + 13*x2*x5 + 21,
            9*x0**2*x2 - 98*x2**2*x4 + 13*x2**2*x7 + 73*x4*x5*x7 - 33*x2*x6*x7,
            -91*x4*x5**2 + 82*x6**2*x7 + 100*x1*x7**2 + 36*x6**2 - 87*x2,
            23*x3**2*x4 + 80*x1*x7**2 - 48*x4*x7**2 - 102*x1**2 - 16*x4*x7 + 87,
            77*x0*x3*x5 - 38*x1*x5**2 - 41*x1*x6*x7 - 39*x5*x6*x7 - 40*x6*x7**2,
            -75*x1*x4**2 + 67*x2*x5**2 + 13*x5**2*x6 - 57*x4*x6 + 60*x2*x7,
            -102*x1**2*x5 - 44*x5**2*x6 + 85*x5**2*x7 + 18*x1*x3 + 101*x6 - 41,
            71*x0**2*x2 - 71*x3*x4**2 + 70*x2*x5**2 + 77*x1*x6**2 - 91*x2*x4*x7,
            -50*x2*x3*x4 - 83*x2*x7**2 - 33*x3*x7**2 - 83*x4,
            -2*x0**2*x4 + 100*x1*x2*x7 - 91*x4*x5*x7 - 18*x0*x6 + 18*x4*x6,
            -87*x0*x4*x5 + 28*x4*x6**2 - 67*x0*x2*x7 - 98*x3**2*x7 - 96*x1*x5*x7 - 74,
            20*x3**2*x7 + 35*x4*x5*x7 + 7*x6**2*x7 - 75*x6*x7**2 - 86*x0**2,
            38*x3**2*x4 + 103*x2*x3*x6 + 21*x0*x5*x7 - 64*x0*x2 + 102*x1*x4 + 4,
            4*x0**2*x1 - 13*x1**2*x4 - 25*x1*x2*x5 + 47*x4*x5**2 + 18*x5**3 - 1,
        ],
        [
            67*x1**2*x3 + 98*x4*x5**2 + 88*x0*x5*x6 + 82*x2*x5*x7 - 92*x3**2,
            -68*x0*x2*x4 - 43*x1*x2*x7 - 97*x0*x4*x7 - 78*x0*x2 + 63*x1*x3 + 25,
            20*x1*x3**2 + 95*x3*x4*x5 + 21*x2**2*x6 + 53*x1*x4*x6 + 11*x4*x5,
            75*x1*x4*x5 + 94*x3*x6**2 - 54*x5*x6**2 + 2*x0*x6*x7 + 58*x6,
            30*x1**3 + 44*x0*x4*x5 + 20*x2*x5*x6 + 81*x6**3 + 6*x7**3,
            41*x3**3 + 57*x0*x1*x4 - 99*x1*x2*x4 + 94*x4*x5**2 - 21*x2*x3*x7 - 54,
            -75*x1*x4*x6 - 58*x2*x3*x7 - 96*x3**2*x7 - 59*x1*x5*x7 - 82*x2*x7**2,
            36*x2*x5*x6 + 85*x6**3 + 89*x0*x4 - 67*x4*x5 - 55*x2*x6,
            -16*x3**2*x4 + 104*x2*x6**2 - 37*x0**2 - 84*x0*x3 - 98*x0*x7,
            45*x2*x4*x5 - 50*x3**2*x6 + 100*x1*x3 - 102*x1*x4 + 9*x6*x7,
            -91*x1**2*x4 - 82*x1**2*x6 + 33*x1*x4*x7 + 10*x5**2*x7 - 81*x5*x6*x7 + 21,
            3*x1*x3**2 + 39*x0*x3*x4 + 72*x0*x7**2 + 65*x0*x5 + 23*x1*x6,
            46*x0**2*x3 - 12*x0**2*x5 + 7*x4*x5*x6 + 77*x2*x7 - 6,
            -72*x0*x2*x5 - 62*x2*x4*x6 - 31*x1*x6*x7 + 5*x1**2 + 61*x3*x7,
            -103*x2*x5*x6 + 53*x3*x6**2 - 45*x0*x6*x7 - 29*x0**2 + 60*x5**2 - 3,
            -104*x0*x1*x2 + 26*x1**2*x6 - 56*x1*x4*x6 + 36*x3*x6*x7 + 83*x7**3 + 185,
        ],
        [
            70*x0*x2*x4 + 92*x0*x1*x7 - 8*x0*x4*x7 - 88*x0*x4 - 2*x4*x7 - 54,
            -91*x1*x2*x5 + 3*x2**2*x5 + 84*x3*x6*x7 + 103*x0*x7**2 + 8*x7**3,
            -77*x0*x2**2 - 17*x3*x4*x6 + 61*x2*x6**2 + 12*x3*x5 - 41*x5*x6 - 123,
            -87*x0**2*x1 + 64*x4*x5*x6 - 20*x4**2*x7 + 48*x4*x6*x7 + 93*x6**2*x7,
            78*x1*x2*x5 + 101*x4**2*x5 + 45*x0*x3*x7 + 51*x5*x6*x7 + 87,
            -22*x2*x3**2 + 57*x0*x3*x4 + 105*x2*x4 - 98*x3*x4 + 54*x3*x7,
            102*x2**2*x3 - 43*x4**2*x5 + 17*x2**2*x6 - 50*x3*x5*x7 - 23*x2*x7**2,
            -22*x0**2*x3 + 99*x1*x5*x6 + 40*x6**3 + 82*x3*x5*x7 - 73,
            -95*x0**2*x1 + 55*x1*x2*x6 - 70*x4*x7**2 + 32*x3**2 + 53*x6**2,
            -8*x0*x1*x4 + 63*x2**2*x4 + 69*x1**2*x5 + 89*x3*x5*x7 + 78*x7 - 2,
            -4*x2*x3*x5 - 104*x0**2*x6 - 58*x0*x5*x6 + 70*x5*x6*x7 + 69*x4,
            -20*x4**3 + 3*x0*x5*x7 - 101*x1*x6*x7 - 15*x3*x7 + 99*x5*x7 + 22,
            10*x1*x3*x5 - 99*x1*x5**2 - 12*x1*x2*x7 + 55*x4**2*x7 + 68*x6 + 12,
            -15*x1**2*x3 + 92*x0*x3**2 + 96*x1*x2*x5 - 79*x3*x6*x7 + 73*x4*x6,
            6*x1**2*x7 + 71*x5**2*x7 + 70*x0*x1 + 3*x4 - 51,
            -86*x1**2*x4 + 30*x1*x5**2 + 51*x2*x3*x6 + 22*x4**2*x6 - 12*x0*x4*x7,
        ],
        [
            60*x2*x3**2 + 39*x1*x4**2 + 72*x2*x5**2 - 26*x1*x5*x6 - 84*x6**3,
            59*x0*x1*x6 - 77*x2*x6**2 + 23*x2*x4*x7 + x2*x3 + 52*x0*x6 + 25,
            15*x1**2*x5 - 105*x1*x6*x7 - 74*x2*x3 - 69*x5**2 - x7**2,
            -12*x1*x4**2 - 93*x1*x4*x5 - 9*x3*x5*x6 - 19*x2*x6*x7 - 78*x1 - 21,
            85*x1*x2*x4 - 82*x2**2*x4 + 77*x1**2*x5 - 74*x0**2*x6 - 69*x1*x6**2,
            12*x0**2*x2 + 35*x0*x1*x5 + 77*x3*x5*x6 + 85*x4*x6*x7 + 89*x0*x2,
            35*x5**3 - 31*x0*x2*x6 + 70*x3*x6**2 + 50*x2*x4*x7 - 19*x5*x6*x7 + 21,
            -25*x0*x3*x5 + 31*x0**2*x7 - 99*x0*x3*x7 - 2*x5*x7**2 + 101*x2*x4,
            8*x2**2*x5 + 80*x3**2*x6 + 55*x1*x4*x6 - 77*x4*x6**2 - 62*x0*x3*x7,
            82*x4*x5**2 + 67*x3**2*x7 - 22*x3*x5*x7 + 40*x6**2*x7 - 85*x0*x1 + 1,
            -9*x3**2*x5 - 64*x2*x7**2 - 46*x2*x5 - x7**2 - 43*x7,
            -59*x1*x3*x5 - 84*x3*x4*x5 - 56*x2*x3*x6 - 79*x0*x4*x6 + 69*x0,
            32*x2**2*x4 + 80*x3**2*x5 - 84*x5**2*x7 + 7*x3*x4,
            -37*x0*x1*x5 - 77*x1*x3*x6 - 62*x1*x5 - 32*x0 + 95,
            57*x1*x2**2 + 24*x3*x4**2 + 91*x0*x1*x5 - 19*x3**2*x5 - 91*x4*x5*x7,
            -33*x0*x2*x4 + 46*x0*x1*x5 - 62*x1**2*x6 - 76*x6*x7**2 + 99*x5*x6 + 21,
        ],
        [
            88*x1**2*x2 - 54*x1*x6*x7 - 83*x4*x6*x7 + 102*x0*x2 - 96*x1*x3,
            2*x1*x2*x3 - 38*x1*x3*x6 - 18*x1*x7 - 54*x6*x7 - 74*x1 + 87,
            -48*x3*x4**2 + 53*x4**3 + 22*x0*x4*x5 - 73*x3*x4*x5 + 5*x2*x6**2,
            -46*x1*x3**2 - 6*x1**2*x5 + 54*x2*x7**2 - 49*x5**2 - 97*x6,
            26*x3*x5**2 - 10*x6**3 + 47*x0*x6*x7 + 39*x6**2 + 21,
            85*x0**2*x1 + 56*x2*x5**2 + 3*x0*x6**2 - 91*x3*x6**2 - 94*x0*x7**2,
            61*x2**2*x3 + 72*x1*x3**2 + 77*x0*x7**2 - 93*x0*x7 + 29,
            -7*x1**3 + 25*x2*x3**2 + 6*x3*x5*x6 + 95*x2*x6*x7 + 88*x4*x7**2 + 10,
            -105*x0*x1*x3 - 56*x0*x2*x6 - 25*x5*x6**2 + 25*x4*x5 + 80*x6*x7,
            -64*x0*x1**2 + 25*x2*x3**2 - 55*x2**2*x5 - 101*x2*x3*x7 - 31*x0*x4*x7,
            13*x1*x2*x6 - 16*x0*x5*x6 + 7*x1*x4*x7 + 102*x5**2 - 53*x3*x6 + 21,
            -98*x1*x2*x5 + 16*x1**2*x7 - 105*x3*x4*x7 + 65*x2*x5*x7,
            94*x1*x2*x4 + 44*x4**2*x6 + x1*x6*x7 + 36*x0*x1 - 13*x5*x7 + 87,
            7*x0*x1*x3 - 96*x0*x3**2 + 5*x0*x4*x5 + 51*x3*x7**2 - 30*x5*x7**2,
            -13*x0*x1*x3 + 15*x0*x4**2 + 76*x3**2*x6 + 86*x0*x7**2 + 17*x5*x6,
            59*x0*x2**2 - 83*x0*x1*x7 + 104*x0*x3*x7 - 38*x2*x4 + 28*x6*x7 + 145,
        ],
        [
            59*x2**2*x7 + 46*x0*x5*x7 + 64*x1**2 + 84*x2*x5 + 85*x7 + 25,
            -17*x1*x2*x3 - 80*x0*x2*x6 - 86*x5**2*x7 - 45*x6*x7**2 - 41*x0*x6 + 74,
            -37*x2**2*x5 - 103*x5**3 - 16*x1*x3*x6 + 86*x4*x6 - 32*x1,
            44*x3**2*x4 + 104*x3*x5**2 + 94*x0*x1*x6 + 82*x3*x6 - 31*x3 + 13,
            -27*x4**2*x6 - 99*x4**2*x7 - 30*x0*x1 - 76*x4*x6 - 7*x3*x7,
            31*x0*x2*x3 + 95*x1*x3**2 - 21*x3*x4**2 + 35*x4*x5*x7 - 86*x4*x7**2,
            -77*x0*x1**2 - 19*x3*x5**2 + 61*x4**2*x7 - 2*x4 + 22*x5 + 12,
            33*x1*x2**2 - 68*x2**2*x5 + 27*x3*x6**2 + 74*x0*x7 + 93*x2*x7,
            59*x2*x5**2 - 48*x3*x6**2 + 56*x1**2*x7 + 78*x1*x7**2 + 29*x0*x6,
            48*x3**3 - 51*x0*x1*x5 - 77*x1*x2*x6 - 40*x6**2*x7 + 45*x2*x3 + 87,
            -72*x0**2*x2 - 30*x0*x2*x6 + 24*x4*x5*x7 + 40*x1*x6*x7 - 46*x4,
            46*x0**2*x7 + 33*x0*x1*x7 + 18*x0*x6*x7 + 17*x2*x7**2 + 91*x0**2,
            -69*x3*x6**2 + 65*x4**2*x7 + 26*x5**2*x7 - 39*x0**2 - 42*x4*x6 + 12,
            -100*x1**2*x2 + 70*x1*x2*x4 - 28*x0*x3*x4 + 20*x1*x3*x4 + 55*x5*x7**2,
            16*x2*x4*x7 - 56*x2*x5*x7 - 53*x0**2 - 6*x0*x6 - 58*x1 + 14,
            60*x0*x4**2 - 97*x0*x5**2 - 49*x0*x1*x6 + 35*x3**2*x7 - 33*x2*x6 + 87,
        ],
        [
            -45*x2**2*x7 - 23*x0*x5 + 67*x6*x7 - 46*x2 - 59*x6,
            -2*x1*x2*x3 - 49*x1*x5**2 + 67*x0*x6**2 + 50*x2*x3*x7 + 36*x1*x2,
            -98*x1*x3**2 + 5*x0*x4*x6 + 2*x1*x3*x7 + 25*x4*x5 - 84*x5 + 25,
            -77*x2**2*x3 + 41*x2**2*x4 + x1*x3*x5 + 54*x1*x6**2 + 69*x0*x4*x7,
            -28*x0*x3*x5 + 61*x2*x5**2 + 8*x2*x5*x7 + 68*x3*x6*x7 + 38*x2*x3 + 21,
            44*x4**2*x5 - 21*x3**2*x7 - 26*x0*x5*x7 - 87*x4*x7**2 + 41*x1*x5,
            -2*x0**2*x3 - 98*x2*x3*x6 + 82*x2*x5*x6 + 55*x1*x5*x7 + 5*x0*x3 + 54,
            90*x3*x4*x5 - 99*x2**2*x6 - 89*x5**2*x6 - 6*x2*x7**2 + 105*x7**2,
            -102*x0**2*x1 + 104*x3*x5**2 + 25*x3*x7**2 - 18*x4*x7**2 - 79*x7**2,
            47*x0*x4**2 - 11*x6**2*x7 + 71*x4*x7**2 - 14*x2*x5 + 15*x2*x6 + 4,
            -84*x1**3 - 8*x0*x1*x6 + 95*x0*x7**2 - 45*x6*x7**2 - 16*x2*x3,
            -6*x2*x5**2 + 102*x0**2*x6 + 53*x0*x1*x6 - 74*x4*x5*x6 - 64*x5*x6,
            -67*x1*x2**2 - 97*x2*x4*x6 - 67*x0*x3*x7 + 78*x4*x5 + 98*x1 - 5,
            -39*x1**2*x2 + 26*x4*x5*x6 - 48*x5**2*x7 - 24*x1*x3 + 48*x3*x5,
            -58*x0**2*x5 + 64*x2*x3*x5 + 33*x2*x4*x6 + 57*x3*x6**2 + 53*x2 + 1,
            -68*x1**3 - 87*x0*x1*x4 - 39*x0*x2*x6 + 88*x2*x5*x7 - 58*x1*x5 + 8,
        ],
        [
            -92*x0**2*x4 + 6*x3*x4*x6 + 56*x0*x5*x6 - 51*x2*x4 + 87*x6 + 87,
            -x0*x3*x5 - 31*x6**3 - 101*x0*x7**2 + 4*x0**2 - 79*x0,
            -97*x4*x5**2 + 93*x3**2*x7 + 81*x0*x3 - 93*x2*x3 + 6*x1*x5 + 12,
            83*x0*x1*x4 + 39*x2*x5**2 + 22*x5*x7**2 - 93*x0**2 - 101*x2*x5,
            -105*x5**3 + 41*x3*x4*x6 + 12*x4*x7**2 - 100*x0*x3 + 12*x0*x6 - 98,
            11*x3**3 - 36*x4**2*x6 + 84*x0*x5*x7 + 21*x5*x6 + 64*x6 - 5,
            -101*x0*x1*x7 + 19*x3*x5*x7 - 13*x2*x4 - 5*x1*x5 + 83*x2*x5 + 4,
            68*x1**2*x2 + 75*x3**3 + 15*x2*x5*x6 - 102*x0*x5 - 96*x4*x6,
            18*x3*x4*x6 + 80*x1*x6**2 - 85*x3*x4*x7 + 99*x5**2*x7 - 69*x4*x7**2 + 12,
            -95*x3*x4*x5 + 25*x0*x1*x6 + 40*x5*x6**2 - 62*x0*x3*x7 + 96*x0*x7**2 + 87,
            99*x1*x2*x4 - 64*x1*x4**2 - 72*x2**2*x7 + x2*x4*x7 - 27*x0*x7,
            -34*x0*x4*x5 + 23*x4**2*x6 + 4*x3*x5*x6 - 39*x2*x6**2 + 80*x3*x6 + 15,
            64*x5**2*x6 - 36*x5*x6**2 + 54*x5*x6*x7 + 105*x2*x4 - 56*x4**2 - 21,
            50*x2**2*x5 + 26*x0*x5*x7 + 102*x0*x6*x7 + 72*x0**2 + 53*x3*x6,
            -19*x0**2*x6 - 88*x3*x4*x6 - 37*x4*x6*x7 + 39*x5*x7**2 - 40*x0 + 28,
            35*x2*x4**2 + 25*x0*x5**2 - 16*x2*x4*x7 + 3*x2*x5 - 83*x6*x7 - 128,
        ],
        [
            -69*x0**2*x1 - 12*x0*x1*x2 + 71*x1*x2*x5 + 29*x4*x6**2 - 35*x6**3 - 254,
            27*x1*x2*x4 - 3*x0**2*x5 - 5*x0*x3*x5 + 30*x1*x3*x5 + 15*x0*x7**2,
            72*x2*x3*x4 + 47*x4**2*x6 + 17*x3*x7 - 47*x5*x7 + 87*x7 - 61,
            15*x1**2*x3 + 83*x3**2*x4 - 7*x2**2*x5 + 93*x1*x6*x7 + 46*x3*x7,
            -14*x1**2*x4 - 8*x1*x2*x5 + 81*x2*x4*x5 - 7*x4*x5*x6 - 71*x3**2*x7,
            52*x0*x3*x5 + 54*x3*x5*x6 + 62*x3*x6**2 - 65*x6**3 + 31*x0*x3*x7 + 25,
            -58*x0**2*x1 + 93*x1*x4*x6 + 87*x3*x4*x7 - 62*x4*x7**2 + 47*x1*x3,
            -95*x0**2*x4 - 68*x0*x4*x5 + 86*x0*x6**2 - 65*x4*x5 + 19*x0*x7,
            69*x3**2*x4 - 59*x3**2*x5 - 8*x0*x3*x7 + 59*x2**2 - 97*x2*x6 + 21,
            4*x0*x2*x3 + 66*x4*x5*x6 + 99*x5**2*x7 - 33*x2*x7**2 - 97*x0,
            -92*x0*x5**2 + 4*x5*x6**2 + 43*x7**3 + 33*x0*x2 + 61*x0*x5 - 77,
            -26*x1**2*x2 + 98*x1*x2*x6 + 98*x0*x2*x7 - 93*x2*x6*x7 - 23,
            86*x2*x5*x6 + 37*x5*x6*x7 - 42*x0*x7**2 - 45*x7**2 + 67*x1,
            -39*x2**3 + 75*x0*x1*x4 + 16*x3**2*x5 + 81*x2*x4*x5 + 17*x2*x6*x7 + 125,
            -24*x0*x2**2 + 22*x0**2*x7 - 95*x0*x7**2 - 22*x4*x5 - 26*x5,
            -85*x1**2*x3 - 47*x1*x5**2 - 78*x2*x3*x6 + 101*x1*x6**2 - 66*x1*x6*x7 + 12,
        ],
        [
            95*x2*x5**2 - 38*x1**2*x7 - 53*x2**2*x7 - 46*x3*x5*x7 + 69*x2**2,
            -58*x0*x3*x5 + 18*x3*x4*x5 + 47*x2*x4*x6 - 67*x1*x7**2 + 16*x1*x3,
            82*x1**3 - 51*x3*x6**2 - 41*x7**3 + 69*x0*x2 + 96*x2*x5 - 1,
            -7*x3*x4*x5 + 86*x4**2*x7 + 100*x5*x6*x7 - 12*x0*x3 + 19*x3*x4 - 7,
            55*x4**3 + 92*x1**2*x7 - 83*x1*x3*x7 + 85*x3*x7**2 + 125,
            -29*x1**3 - 5*x3**2*x5 - 21*x3*x5**2 - 40*x1*x4*x6 - 100*x3**2*x7 - 6,
            -48*x0*x2*x3 + 10*x4**3 + 55*x0*x4*x5 + 104*x4**2*x7 + 20*x3,
            -46*x0*x2*x5 + 71*x1*x6*x7 + 82*x2*x7**2 + 60*x3**2 + 22*x2*x6 + 4,
            45*x0**2*x2 + 42*x3**2*x4 - 2*x4**3 - 11*x1*x5**2 + 39*x4*x7**2,
            -34*x0**2*x1 - 4*x2**2*x5 + 36*x2*x3*x7 - 60*x0*x5*x7 + 53*x1*x5*x7 + 2,
            55*x0*x2*x3 - 94*x0**2*x4 - 66*x4**3 - 87*x2*x5*x6 + 56*x6**2*x7,
            79*x4*x5**2 - 3*x3*x4*x7 + 64*x0*x5*x7 - 27*x2*x7**2 + 8,
            -101*x0*x2*x4 - 52*x3**2*x7 + 93*x0*x6 + 18*x0 - 67*x5 - 128,
            -92*x0*x1*x2 + 43*x0*x3**2 - 96*x0*x1*x7 - 33*x2*x7**2 - x0*x6,
            -64*x2*x4*x7 + 26*x5**2*x7 - 80*x5*x6*x7 + 95*x2*x7**2 - 104*x3*x5 + 184,
            -31*x3*x5*x6 + 101*x0*x6**2 - 71*x3*x6**2 + 72*x1*x5 + 55*x4*x6,
        ],
        [
            -72*x1*x3*x4 - 56*x3**2*x4 + 2*x0*x4*x5 + 67*x3**2*x6 + 69*x3*x7**2,
            68*x0*x1**2 - 74*x0*x1*x2 + 44*x1*x4**2 + 36*x0*x5 + 43*x6*x7 + 98,
            -59*x1**2*x5 + 91*x2*x3*x6 + 100*x0*x5*x7 - 88*x4 - 14*x7,
            -85*x0*x2*x3 - 54*x5*x6**2 - 53*x0*x3*x7 + 72*x1*x5*x7 + 63*x7 + 21,
            3*x1*x2**2 + 52*x4*x5**2 + 86*x2*x3*x7 - 34*x1**2 - 42*x3*x7,
            19*x0*x1*x4 + 25*x2*x4**2 - 105*x1*x3*x6 + 93*x1*x6**2 - 79*x3**2,
            -x0**2*x2 + 79*x1*x3*x4 + 42*x3**2*x5 - 47*x3*x5**2 + 76*x2*x6**2 + 25,
            -14*x1**3 - 103*x4*x5**2 - 40*x1*x4*x6 + 51*x1**2*x7 + 31*x4**2,
            84*x1**3 + 8*x0**2*x3 + 20*x0*x1*x3 - 40*x3*x4*x5 + 84*x0**2,
            23*x4*x5**2 - 79*x4*x5*x6 + 96*x4**2*x7 + 51*x5**2*x7 - 31*x0*x2,
            51*x1*x5*x7 - 30*x5**2*x7 - 4*x0*x4 + 48*x2*x4 - 4*x3*x7 + 12,
            66*x3*x5*x7 - 29*x3**2 + 5*x2*x6 + 101*x2*x7 - 22*x4,
            38*x0**2*x3 - 85*x2*x5**2 - 10*x0*x3*x7 + 39*x5**2*x7 + 35*x2**2 + 15,
            83*x1*x3*x5 + 61*x4**2*x5 + 85*x1**2*x7 - 25*x5*x6 + 67*x0*x7,
            7*x1*x3**2 + 78*x1*x4*x5 - 94*x4*x7**2 + x1*x5 + 44*x1 + 145,
            -26*x1**2*x2 - 13*x0**2*x4 + 39*x0*x2*x5 - 95*x4*x7**2 - 6*x0*x6 + 12,
        ],
        [
            88*x1*x5**2 - 46*x0**2*x6 + 70*x0*x3*x7 + 52*x6*x7**2 - 52*x3*x4 + 1,
            -4*x1**2*x4 - 13*x5**3 + 26*x2*x5*x7 - 95*x4*x6*x7 - 23*x3*x6,
            7*x1**2*x4 - 13*x1*x3*x4 + 103*x2*x3*x4 - 9*x2*x5**2 - 42*x3*x7**2 + 3,
            -78*x1**3 + 97*x2*x3*x6 + 27*x1*x5*x6 + 65*x1*x3*x7 - 43*x5,
            54*x0**2*x4 - 76*x2**2*x6 - 91*x1*x6*x7 + 26*x0*x2 - 9*x2**2 + 87,
            -52*x1**2*x5 - 54*x2*x3*x5 - 77*x2**2*x7 + 66*x3*x6*x7 - 19*x1*x6,
            -43*x0*x3*x4 - 14*x2*x4*x5 + 45*x0*x4*x6 - 29*x0**2*x7 - 52*x3*x7,
            -78*x0**2*x1 + 46*x0*x2*x5 - 60*x4**2*x5 - 67*x1*x6*x7 - 41*x4**2 + 7,
            34*x1**2*x3 - 63*x3**2*x6 + 2*x2*x4*x6 - 9*x3*x5*x6 + 41*x3*x4 - 114,
            100*x1*x2*x3 - 42*x6**3 - 45*x2*x5*x7 - 10*x3*x4 + 67*x2*x7,
            -72*x1**2*x2 - 30*x1*x2**2 + 63*x0*x3*x6 + 12*x2*x6*x7 + 46*x4*x5 + 21,
            89*x5**3 - 101*x4*x5*x6 + 15*x7**3 + 24*x2**2 - 47*x2*x7,
            -97*x4**3 - 14*x3**2*x6 + 46*x3*x4*x6 - 10*x3*x6**2 + 75*x6*x7**2 - 87,
            -54*x0*x1**2 - 5*x0*x3*x6 + 89*x2*x4*x7 + 17*x1*x7**2 + 60*x4**2 + 21,
            45*x1*x3*x5 - 81*x5*x6**2 - 36*x3*x4 + 15*x3*x5 + 7*x6**2 + 98,
            56*x4**2*x6 + 58*x0*x7**2 - 47*x1*x2 + 26*x6 + 103,
        ],
    ]
