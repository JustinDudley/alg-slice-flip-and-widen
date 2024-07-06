
import pandas as pd 
from variables import *  
from methods import *


print("\n\ndf_complements_and_inverses:\n\n", df_complements_and_inverses, "\n")
print("df_Ripple_R:\n\n", df_Ripple_L, "\n")
print("df_Ripple_L:\n\n", df_Ripple_R, "\n")

print("df_turns:\n\n", df_turns, "\n")
print("df_rotations:\n\n", df_rotations, "\n")
print("df_reflections:\n\n", df_reflections, "\n")


# to find a value in dataframe using  .at
print("The complement of R' is: ", df_complements_and_inverses.at["R'", "complement"])



group_number = 1    # Must choose a group before running program. (1-6)
alg = "U R2 U D' F B L' B2 R U D' B R L' U2 B2"


alg = condense_comp_slice_turns(alg)    # In this example:   U R2 UD' F B L' B2 R UD' B RL' U2 B2
alg_trailing_WCRs = group_dict[group_number]
alg_turns = alg.split()
trailing_WCRs = alg_trailing_WCRs.split()



slice_opportunity_positions = []
for i in range(len(slice_comps)):
	for j in range(len(alg_turns)):
		if slice_comps[i]==alg_turns[j]:
			slice_opportunity_positions.append(j)

slice_opportunity_positions = sorted(set(slice_opportunity_positions))
print("slice opportunity positions: ", slice_opportunity_positions)


# while intersection_has_members(slice_comp, alg_turns)
if intersection_has_members(slice_comps, alg_turns):
	for position in slice_opportunity_positions:
		print("yo", alg_turns[position])
		alg_turns[position] = df_complements_and_inverses.at[alg_turns[position], "complement"]
		print("yo", alg_turns[position])




# iterating over slice_comps
# getting access to element AND index within a loop. Use "enumerate" method, and use string interpolation:
# THIS WILL BE THE OUTER LOOP IN MY DOUBLE-NESTED (3-LAYER) LOOP
for index, slice_comp in enumerate(slice_comps):
	print("At index %s we have %s"%(index, slice_comp)  )
	if slice_comp in alg_turns:
		target_index = alg_turns.index(slice_comp)
		alg_turns[target_index] = slice_comp + "yoyo"
		print(alg_turns)
		for idx, alg_turn in enumerate(alg_turns):
			if idx > target_index:
				alg_turn = alg_turn + "9"
				print(alg_turn)
		# for index, alg_turn in enumerate(alg_turns):
			# print("index: ", index, " alg_turn: ", alg_turn)
		# i believe the second nested loop goes here?
		print("yes, this slice_comp is in the alg")
	else:
		print("no, this slice_comp isn't in the alg")

print(alg_turns)
