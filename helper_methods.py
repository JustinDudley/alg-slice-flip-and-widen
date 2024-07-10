
from constants import SLICE_COMP_CONDENSER_DICT
from dataframes import df_comp_rotation_nums


# R L' -->  RL',  D U' --> U'D, etc.   This block condenses slice comps into a single turn, with no space in the middle
def condense_comp_slice_turns(alg):
    for key, value in SLICE_COMP_CONDENSER_DICT.items():
        alg = alg.replace(key, value).rstrip()
    return alg
     


def get_comp_turn_codes(turn):
    if turn in df_comp_rotation_nums.index:
        return int(df_comp_rotation_nums.at[turn, "comp_rotation_num"])
    else:
        return 0








# NOT IN USE. But the coding is pretty cool. Found it on the interweb:
# def intersection_has_members(list1, list2):
#     temp = set(list2)
#     shared_members = [value for value in list1 if value in temp]
	
#     if shared_members:    # the if operator returns true in Python for any data structure that is non-empty
#         return True
#     else: 
#         return False 

