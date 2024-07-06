
from variables import *  


# R L' -->  RL',  D U' --> U'D, etc.   This block condenses slice comps into a single turn, with no space in the middle
def condense_comp_slice_turns(alg):
    for key, value in slice_comp_condenser_dict.items():
        alg = alg.replace(key, value)
    return alg
     

def intersection_has_members(list1, list2):
    temp = set(list2)
    shared_members = [value for value in list1 if value in temp]
	
    if shared_members:    # the if operator returns true in Python for any data structure that is non-empty
        return True
    else: 
        return False 



def ripple_right(turn, WCR):
	column = "%sA-->B%s"%(WCR, WCR)
	return df_Ripple_R.at[turn, column]

def ripple_right_WCR_list(turn, WCR_list):
	for WCR in WCR_list:
		turn = ripple_right(turn, WCR)
	return turn