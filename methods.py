
from variables import SLICE_COMP_CONDENSER_DICT


# R L' -->  RL',  D U' --> U'D, etc.   This block condenses slice comps into a single turn, with no space in the middle
def condense_comp_slice_turns(alg):
    for key, value in SLICE_COMP_CONDENSER_DICT.items():
        alg = alg.replace(key, value).rstrip()
    return alg
     




# NOT IN USE. But the coding is pretty cool. Found it on the interweb:
# def intersection_has_members(list1, list2):
#     temp = set(list2)
#     shared_members = [value for value in list1 if value in temp]
	
#     if shared_members:    # the if operator returns true in Python for any data structure that is non-empty
#         return True
#     else: 
#         return False 

