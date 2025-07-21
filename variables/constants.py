
# Python doesn't support constants, but by convention UPPERCASE vars are understood to be constants



ROTATION_VECTOR = "rotation_vector"
COMPLEMENT = "complement"


SOLVED_PATTERN_LETTERS = ["wht", "grn", "red", "blu", "ora", "yel", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"]

STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_1 = ["X", "U", "V", "W", "B", "C", "D", "A"]
STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_2 = ["V", "W", "X", "U", "D", "A", "B", "C"]
STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_3 = ["P", "M", "N", "O", "H", "E", "F", "G"]
STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_4 = ["F", "G", "H", "E", "N", "O", "P", "M"]
STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_5 = ["K", "L", "I", "J", "Q", "R", "S", "T"]
STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_6 = ["Q", "R", "S", "T", "K", "L", "I", "J"]



INTERNAL_X_INVERSE_DICT = {
	"X": "X'",
	"X2": "X2",
	"X'": "X"
}


# this constnat is SPECIFIC TO THE INTERNAL_X BRANCH
# an X within an alg DOES NOT indicate that we are looking for complementary turns
# this never presented a problem in other branches, but it does here because the algs are full of internal X
# so, the method "get_single_turn_code" can't use the "CODE" constant. It must use THIS constant instead
GET_CODE_FROM_TURN = {
    "R": 1,
    "r": 1,
    "l'": 1,
    "L'": 1,
    "R2": 2,
    "r2": 2,
    "l2": 2,
    "L2": 2,
    "R'": 3,
    "r'": 3,
    "l": 3,
    "L": 3
}


CODE = {
    0: "X0",
    1: "X",
    2: "X2",
    3: "X'",
    "X0": 0,
    "X": 1,
    "R": 1,
    "r": 1,
    "l'": 1,
    "L'": 1,
    "X2": 2,
    "R2": 2,
    "r2": 2,
    "l2": 2,
    "L2": 2,
    "X'": 3,
    "R'": 3,
    "r'": 3,
    "l": 3,
    "L": 3
}




# note the intentional white space after the second turn of the key (AND value), when there is no prime (')
SLICE_COMP_COMPOUNDIFIER_DICT = {
    "R L'": "RL'", 
    "L' R ": "RL' ", 
    "R' L ": "R'L ", 
    "L R'": "R'L",
    "R2 L2": "R2L2", 
    "L2 R2": "R2L2",
    "U D'": "UD'", 
    "D' U ": "UD' ", 
    "U' D ": "U'D ", 
    "D U'": "U'D",
    "U2 D2": "U2D2", 
    "D2 U2": "U2D2",
    "F B'": "FB'", 
    "B' F ": "FB' ", 
    "F' B ": "F'B ", 
    "B F'": "F'B",
    "F2 B2": "F2B2",
    "B2 F2": "F2B2"
}

SLICE_COMPS = list(SLICE_COMP_COMPOUNDIFIER_DICT.values())   # this is how you create a list from dictionary values



# each key's value is the cube rotation that moves the sticker Q to the key
# the values are in Alg--YorZ--X format (without the Alg)
# Note that this dictionary is not related to analyzing a cube with swapped pieces. It is a separate concept where a solved
# cube is rotated several times (as many times as the number of WCRs in trailing_WCRs) and we see where sticker Q ends up. 
# So this is robust dictionary and can handle any pair swap.
WHAT_BRINGS_Q_HERE = {
    "A": [["Y2", "X"], ["Z2", "X'"]], 
    "B": [["Z", "X'"]], 
    "C": [["Y0", "X'"]], 
    "D": [["Z'", "X'"]], 
    "E": [["Y'", "X0"]], 
    "F": [["Y'", "X'"]], 
    "G": [["Y'", "X2"]], 
    "H": [["Y'", "X"]], 
    "I": [["Y2", "X0"], ["Z2", "X2"]], 
    "J": [["Z", "X2"]], 
    "K": [["Y0", "X2"]], 
    "L": [["Z'", "X2"]], 
    "M": [["Y", "X0"]], 
    "N": [["Y", "X"]], 
    "O": [["Y", "X2"]], 
    "P": [["Y", "X'"]], 
    "Q": [["Y0", "X0"]], 
    "R": [["Z'", "X0"]], 
    "S": [["Z2", "X0"], ["Y2", "X2"]], 
    "T": [["Z", "X0"]], 
    "U": [["Y2", "X'"], ["Z2", "X"]], 
    "V": [["Z", "X"]], 
    "W": [["Y0", "X"]], 
    "X": [["Z'", "X"]]
}


# SPECIFIC TO THIS BRANCH
# CLOSELY RELATED TO WHAT_BRINGS_Q_HERE
# ONLY CONCERNED WITH X, X2, X', X0
WHAT_BRINGS_U_HERE = {
    "I": "X", 
    "A": "X2", 
    "S": "X'",
    "U": "X0"
}


GROUP_DICT = {
    1: ["X2", "Y"],
    2: ["X2", "Y'"],
    3: ["Y2", "Z"],
    4: ["Y2", "Z'"],
    5: ["Z2", "X"],
    6: ["Z2", "X'"]
}



AXIS_FAMILY = {
    "R": "X",
    "r": "X",
    "T": "X",
    "l": "X",
    "L": "X",
    "X": "X",
    "R'": "X",
    "r'": "X",
    "T'": "X",
    "l'": "X",
    "L'": "X",
    "X'": "X",
    "R2": "X",
    "r2": "X",
    "T2": "X",
    "l2": "X",
    "L2": "X",
    "X2": "X",
    "X0": "X",
    "F": "Z",
    "f": "Z",
    "S": "Z",
    "b": "Z",
    "B": "Z",
    "Z": "Z",
    "F'": "Z",
    "f'": "Z",
    "S'": "Z",
    "b'": "Z",
    "B'": "Z",
    "Z'": "Z",
    "F2": "Z",
    "f2": "Z",
    "S2": "Z",
    "b2": "Z",
    "B2": "Z",
    "Z2": "Z",
    "Z0": "Z",
    "U": "Y",
    "u": "Y",
    "H": "Y",
    "d": "Y",
    "D": "Y",
    "Y": "Y",
    "U'": "Y",
    "u'": "Y",
    "H'": "Y",
    "d'": "Y",
    "D'": "Y",
    "Y'": "Y",
    "U2": "Y",
    "u2": "Y",
    "H2": "Y",
    "d2": "Y",
    "D2": "Y",
    "Y2": "Y",
    "Y0": "Y"
}


MERGE_YU_DICT = {
	"Y D ": "u ",
	"D Y ": "u ",
	"Y' D'": "u'",
	"D' Y'": "u'",
	"Y2 D2": "u2",
	"D2 Y2": "u2",
	"Y' U ": "d ",
	"U Y'": "d",
	"Y U'": "d'",
	"U' Y ": "d' ",
	"Y2 U2": "d2",
	"U2 Y2": "d2",
	"Z B ": "f ",
	"B Z ": "f ",
	"Z' B'": "f'",
	"B' Z'": "f'",
	"Z2 B2": "f2",
	"B2 Z2": "f2",
	"Z' F ": "b ",
	"F Z'": "b",
	"Z F'": "b'",
	"F' Z ": "b' ",
	"Z2 F2": "b2",
	"F2 Z2": "b2"
}


REPLACEMENTS_DICT = {
"2'": "2",
"M ": "T' ",
"M2": "T2",
"M'": "T",
"E ": "H' ",
"E2": "H2",
"E'": "H",
"x": "X",
"y": "Y",
"z": "Z",
"(": " ",
")": " ",
"[": " ",
"]": " "
}


HEADER = {
    "I": "I",
    "X": "X",
    "X2": "X2",
    "X'": "X'",
    "X0": "X0",
    "Y": "Y",
    "Y2": "Y2",
    "Y'": "Y'",
    "Y0": "Y0",
    "Z": "Z",
    "Z2": "Z2",
    "Z'": "Z'",
    "Z0": "Z0",
    "R": "R",
    "R2": "R2",
    "R'": "R'",
    "L": "L",
    "L2": "L2",
    "L'": "L'",
    "T": "T",
    "T2": "T2",
    "T'": "T'",
    "r": "r-lower",
    "r'": "r'-lower",
    "r2": "r2-lower",
    "l": "l-lower",
    "l'": "l'-lower",
    "l2": "l2-lower",
    "RL'": "RL'",
    "R2L2": "R2L2",
    "R'L": "R'L",
    "U": "U",
    "U2": "U2",
    "U'": "U'",
    "D": "D",
    "D2": "D2",
    "D'": "D'",
    "H": "H",
    "H2": "H2",
    "H'": "H'",
    "u": "u-lower",
    "u'": "u'-lower",
    "u2": "u2-lower",
    "d": "d-lower",
    "d'": "d'-lower",
    "d2": "d2-lower",
    "UD'": "UD'",
    "U2D2": "U2D2",
    "U'D": "U'D",
    "F": "F",
    "F2": "F2",
    "F'": "F'",
    "B": "B",
    "B2": "B2",
    "B'": "B'",
    "S": "S",
    "S2": "S2",
    "S'": "S'",
    "f": "f-lower",
    "f'": "f'-lower",
    "f2": "f2-lower",
    "b": "b-lower",
    "b'": "b'-lower",
    "b2": "b2-lower",
    "FB'": "FB'",
    "F2B2": "F2B2",
    "F'B": "F'B"
}


# not yet used:
ITERATIVE_DELTA_SWAP_DICT = {
    "R L ":"L** R ",
    "L R ":"R L ",
    "L** R ":"L R ",

    "R L2":"L2** R",
    "L2 R ":"R L2 ",
    "L2** R":"L2 R",

    "R' L'":"L'** R'",
    "L' R'":"R' L'",
    "L'** R'":"L' R'",

    "R' L2":"L2** R'",
    "L2 R'":"R' L2",
    "L2** R'":"L2 R'",

    "R2 L ":"L** R2 ",
    "L R2":"R2 L",
    "L** R2 ":"L R2 ",

    "R2 L'":"L'** R2",
    "L' R2":"R2 L'",
    "L'** R2":"L' R2",


    "U D ":"D** U ",
    "D U ":"U D ",
    "D** U ":"D U ",

    "U D2":"D2** U",
    "D2 U ":"U D2 ",
    "D2** U":"D2 U",

    "U' D'":"D'** U'",
    "D' U'":"U' D'",
    "D'** U'":"D' U'",

    "U' D2":"D2** U'",
    "D2 U'":"U' D2",
    "D2** U'":"D2 U'",

    "U2 D ":"D** U2 ",
    "D U2":"U2 D",
    "D** U2 ":"D U2 ",

    "U2 D'":"D'** U2",
    "D' U2":"U2 D'",
    "D'** U2":"D' U2",


    "F B ":"B** F ",
    "B F ":"F B ",
    "B** F ":"B F ",

    "F B2":"B2** F",
    "B2 F ":"F B2 ",
    "B2** F":"B2 F",

    "F' B'":"B'** F'",
    "B' F'":"F' B'",
    "B'** F'":"B' F'",

    "F' B2":"B2** F'",
    "B2 F'":"F' B2",
    "B2** F'":"B2 F'",

    "F2 B ":"B** F2 ",
    "B F2":"F2 B",
    "B** F2 ":"B F2 ",

    "F2 B'":"B'** F2",
    "B' F2":"F2 B'",
    "B'** F2":"B' F2",
}


GROUP_DICT_HANDY_FOR_SEEING_YorZ_NOTATION_BUT_DEPRECATED = {
    1: [["Y'", "X2"]],
    2: [["Y", "X2"]],
    3: [["Z", "X2"]],
    4: [["Z'", "X2"]],
    5: [["Y2", "X'"], ["Z2", "X"]],
    6: [["Y2", "X"], ["Z2", "X'"]]
}
