
import pandas as pd 
from variables import *  
from methods import *


# print("\n\ndf_complements_and_inverses:\n\n", df_complements_and_inverses, "\n")
# print("df_Ripple_R:\n\n", df_Ripple_L, "\n")
# print("df_Ripple_L:\n\n", df_Ripple_R, "\n")

# print("df_stickers_turned:\n\n", df_stickers_turned, "\n")
# print("df_stickers_rotated:\n\n", df_stickers_rotated, "\n")
# print("df_stickers_reflected:\n\n", df_stickers_reflected, "\n")



group_number = 1    # Must choose a group before running program. (1-6)
alg = "U R2 U D' F B L' B2 R U D' B R L' U2 B2"


alg = condense_comp_slice_turns(alg)    # In this example:   U R2 UD' F B L' B2 R UD' B RL' U2 B2
alg_turns = alg.split()
trailing_WCRs = group_dict[group_number]  # NOTE! At this point, there is no need for dual CoRo schemes or for any standardized way of writing the CoRo. They will all crunch down the same 



slice_opportunity_positions = []
for i in range(len(slice_comps)):
	for j in range(len(alg_turns)):
		if slice_comps[i]==alg_turns[j]:
			slice_opportunity_positions.append(j)

slice_opportunity_positions = sorted(set(slice_opportunity_positions), reverse=True)  # Reversed so that pre-pending the WCRs works.
print("slice opportunity positions: ", slice_opportunity_positions)
# What happens if slice_opportunity_positions is empty?  Do I need to account for this?


# "while" loop not necessary. Do I even need this "if" statement??
# if intersection_has_members(slice_comps, alg_turns):    # Can delete this whole method, right?? Maybe keep for reference
if slice_opportunity_positions:  # returns True if a Python list has members
	for position in slice_opportunity_positions:
		WCR_to_ripple = df_complements_and_inverses.at[alg_turns[position], "rotation_direction"]
		alg_turns[position] = df_complements_and_inverses.at[alg_turns[position], "complement"]  # sub in the complement (a slice)
		for index, alg_turn in enumerate(alg_turns):
			if index > position:
				alg_turns[index] = ripple_right(alg_turns[index], WCR_to_ripple)
		trailing_WCRs = [WCR_to_ripple] + trailing_WCRs

print(alg_turns)
print(trailing_WCRs)




def move_sticker_once(sticker, WCR):
	return df_stickers_turned.at(sticker, WCR)


# def find_a_match
def move_Q_several_times(WCRs):
	sticker = "Q"
	for WCR in WCRs:
		sticker = move_sticker_once(sticker, WCR)
	trailing_WCR = places_Q_goes[sticker]
	return trailing_WCR
def find_match_for_incoming_wcr(WCR):
	sticker = "Q"
	sticker_goes_to = df_stickers_turned.at
	return 1
print(find_match_for_incoming_wcr([5,6]))







#HALF-DEPRECATED, HALF-USEFUL
# iterating over slice_comps
# getting access to element AND index within a loop. Use "enumerate" method, and use string interpolation:
# THIS WILL BE THE OUTER LOOP IN MY DOUBLE-NESTED (3-LAYER) LOOP





# for index, slice_comp in enumerate(slice_comps):
# 	print("At index %s we have %s"%(index, slice_comp)  )
# 	if slice_comp in alg_turns:
# 		target_index = alg_turns.index(slice_comp)
# 		alg_turns[target_index] = slice_comp + "yoyo"
# 		print(alg_turns)
# 		for idx, alg_turn in enumerate(alg_turns):
# 			if idx > target_index:
# 				alg_turn = alg_turn + "9"
# 				print(alg_turn)
# 		# for index, alg_turn in enumerate(alg_turns):
# 			# print("index: ", index, " alg_turn: ", alg_turn)
# 		# i believe the second nested loop goes here?
# 		print("yes, this slice_comp is in the alg")
# 	else:
# 		print("no, this slice_comp isn't in the alg")

# print(alg_turns)
