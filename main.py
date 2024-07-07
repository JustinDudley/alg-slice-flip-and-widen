
import pandas as pd 
from variables import *  
from methods import *


# print("\n\ndf_complements_and_inverses:\n\n", df_complements_and_inverses, "\n")
# print("df_Ripple_R:\n\n", df_Ripple_L, "\n")
# print("df_Ripple_L:\n\n", df_Ripple_R, "\n")

# print("df_stickers_turned:\n\n", df_stickers_turned, "\n")
# print("df_stickers_rotated:\n\n", df_stickers_rotated, "\n")
# print("df_stickers_reflected:\n\n", df_stickers_reflected, "\n")



group_number = 6    # Must choose a group before running program. (1-6)
alg = "U2 L F B' U' R2 L B' U2 F U' D R' U2 L B'"
# alg = "U R2 U D' F B L' B2 R U D' B R L' U2 B2"  ,  group 1



alg = condense_comp_slice_turns(alg)    # For instance:   U R2 UD' F B L' B2 R UD' B RL' U2 B2
alg_turns = alg.split()
trailing_WCRs = group_dict[group_number]  # NOTE! At this point, there is no need for dual CoRo schemes or for any standardized way of writing the CoRo. They will all crunch down the same 



slice_opportunity_positions = []
for i in range(len(slice_comps)):
	for j in range(len(alg_turns)):
		if slice_comps[i] == alg_turns[j]:
			slice_opportunity_positions.append(j)

slice_opportunity_positions = sorted(set(slice_opportunity_positions), reverse=True)  # Reversed so that pre-pending the WCRs works.
print("\nslice opportunity positions: ", slice_opportunity_positions)
# What happens if slice_opportunity_positions is empty?  Do I need to account for this?



# Do I even need this IF statement??
if slice_opportunity_positions:  # returns True if a Python list is non-empty
	for position in slice_opportunity_positions:
		WCR_to_ripple = df_complements_and_inverses.at[alg_turns[position], "rotation_direction"]
		alg_turns[position] = df_complements_and_inverses.at[alg_turns[position], "complement"]  # sub in the complement (a slice)
		for index, alg_turn in enumerate(alg_turns):
			if index > position:
				alg_turns[index] = ripple_right(alg_turns[index], WCR_to_ripple)
		trailing_WCRs = [WCR_to_ripple] + trailing_WCRs



print(alg_turns)
print(trailing_WCRs)

trailing_WCRs_dual = replace_Trailing_WCRs_with_up_to_TWO_equivalent_YorZ_notations(trailing_WCRs)

print(trailing_WCRs_dual)
print("\n")

