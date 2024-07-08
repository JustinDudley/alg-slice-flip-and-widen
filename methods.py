
from variables import *  


# R L' -->  RL',  D U' --> U'D, etc.   This block condenses slice comps into a single turn, with no space in the middle
def condense_comp_slice_turns(alg):
    for key, value in slice_comp_condenser_dict.items():
        alg = alg.replace(key, value).rstrip()
    return alg
     



def ripple_right(turn, WCR):
	column = "%sA-->B%s"%(WCR, WCR)
	return df_Ripple_R.at[turn, column]

def ripple_right_WCR_list(turn, WCR_list):
	for WCR in WCR_list:
		turn = ripple_right(turn, WCR)
	return turn




def move_sticker_once(sticker, WCR):
	## !!!  The line below used to say df_sticker_rotated. I changed it when I added Y0  and X0 as column names of df_sticker_rotated
	## !!!  Need to check that this still works!
	return df_stickers_turned.at[sticker, WCR]

def replace_Trailing_WCRs_with_up_to_TWO_equivalent_YorZ_notations(WCRs):
	sticker = "Q"
	for WCR in WCRs:
		sticker = move_sticker_once(sticker, WCR)
	trailing_WCRs_dual = what_brings_Q_here[sticker]
	return trailing_WCRs_dual



# NOT IN USE. But the coding is pretty cool. Found it on the interweb:
# def intersection_has_members(list1, list2):
#     temp = set(list2)
#     shared_members = [value for value in list1 if value in temp]
	
#     if shared_members:    # the if operator returns true in Python for any data structure that is non-empty
#         return True
#     else: 
#         return False 

