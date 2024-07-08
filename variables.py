import pandas as pd 

df_complements_and_inverses = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/complements_and_inverses.csv', index_col="orig")
df_Ripple_L = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/WCR_Ripples_Left.csv', index_col="orig") 
df_Ripple_R = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/WCR_Ripples_Right.csv', index_col="orig") 

df_stickers_turned = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/stickers_turned_by_alg_notation.csv', index_col="orig") 
df_stickers_rotated = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/stickers_rotated_24.csv', index_col="orig") 
df_stickers_reflected = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/stickers_reflected_24.csv', index_col="orig")


# note the intentional white space after the second turn of the key (AND value), when there is no prime (')
slice_comp_condenser_dict = {
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

slice_comps = list(slice_comp_condenser_dict.values())   # this is how you create a list from dictionary values


# each key's value is the cube rotation that moves the sticker Q to the key
# the keys are in Alg--YorZ--X format (without the Alg)
what_brings_Q_here = {
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



group_dict = {
    1: ["X2", "Y"],
    2: ["X2", "Y'"],
    3: ["Y2", "Z"],
    4: ["Y2", "Z'"],
    5: ["Z2", "X"],
    6: ["Z2", "X'"]
    }




group_dict_handy_for_seeing_standard_notation_but_deprecated = {
    1: [["Y'", "X2"]],
    2: [["Y", "X2"]],
    3: [["Z", "X2"]],
    4: [["Z'", "X2"]],
    5: [["Y2", "X'"], ["Z2", "X"]],
    6: [["Y2", "X"], ["Z2", "X'"]]
    }