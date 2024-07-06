import pandas as pd 

df_complements_and_inverses = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/complements_and_inverses.csv', index_col="orig")
df_Ripple_L = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/WCR_Ripples_Left.csv', index_col="orig") 
df_Ripple_R = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/WCR_Ripples_Right.csv', index_col="orig") 

df_turns = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/turns.csv', index_col="orig") 
df_rotations = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/rotations_24.csv', index_col="orig") 
df_reflections = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/reflections_24.csv', index_col="orig")


slice_comp_condenser_dict = {
    "R L'": "RL'", 
    "L' R": "RL'", 
    "R' L": "R'L", 
    "L R'": "R'L",
    "R2 L2": "R2L2", 
    "L2 R2": "R2L2",
    "U D'": "UD'", 
    "D' U": "UD'", 
    "U' D": "U'D", 
    "D U'": "U'D",
    "U2 D2": "U2D2", 
    "D2 U2": "U2D2",
    "F B'": "FB'", 
    "B' F": "FB'", 
    "F' B": "F'B", 
    "B F'": "F'B",
    "F2 B2": "F2B2",
    "B2 F2": "F2B2"
    }

slice_comps = list(slice_comp_condenser_dict.values())   # this is how you create a list from dictionary values

slice_comp_dict_with_slashes_deprecated_delete_soon = {
    "R L\'": "RL\'", 
    "L\' R": "RL\'", 
    "R\' L": "R'L", 
    "L R\'": "R\'L",
    "R2 L2": "R2L2", 
    "L2 R2": "R2L2",
    "U D\'": "UD\'", 
    "D\' U": "UD\'", 
    "U\' D": "U'D", 
    "D U\'": "U\'D",
    "U2 D2": "U2D2", 
    "D2 U2": "U2D2",
    "F B\'": "FB\'", 
    "B\' F": "FB\'", 
    "F\' B": "F'B", 
    "B F\'": "F\'B",
    "F2 B2": "F2B2",
    "B2 F2": "F2B2"
    }

group_dict = {
    1: "X2 Y",
    2: "X2 Y'",
    3: "Y2 Z",
    4: "Y2 Z'",
    5: "Z2 X",
    6: "Z2 X'"
    }
