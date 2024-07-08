
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

# I haven't yet chanced upon an alg that yielded a dual WCR, so I should keep testing to make sure that works okay




#########
#########
#########
#########      from the Excel file with "PYTHON IN EXCEL"

# Step 1:  Give a value to RotationNum, such as 1,2,...
# Step 2:  Excel created comp_turn_codes (a Python list),   [0, 0, 0, 3, 1, 0, 0, 2, 0, 3, 1, 0, 1, 3, 0, 0, 2]
#so:
RotationNum = 1   # in this NEW python program, this will be deterrmined by the X element of alg--YorZ--X
comp_turn_codes = [0, 0, 0, 3, 1, 0, 0, 2, 0, 3, 1, 0, 1, 3, 0, 0, 2]   # easy to derive from the alg

# RIGHT NOW, THERE IS A MISMATCH BETWEEN ROTATIONNUM ("1") AND THE VERBIAGE OF "2" 

import itertools
import math

positions = []
for i in range (0, len(comp_turn_codes)):
	if comp_turn_codes[i] >0:
		positions.append(i)
	

combs= []
for i in range(1, len(positions)+1):
	els = [list(x) for x in itertools.combinations(positions, i)]
	combs.extend(els)
#print("\nAll position combinations of non-zero elements:  ")
#print(combs)


#
#  !!  Regarding "two_mod_4_combs" and "sum_of_2s":  TWO is no longer the only number used. I can use 0,1,2,or 3 via RotationNum. But I am retaining the variable names for now
#

two_mod_4_combs = []
for comb in combs:
	sum = 0
	for p in comb:
		sum = sum + comp_turn_codes[p]
	if math.fmod(sum,4) == RotationNum:
		two_mod_4_combs.append(comb)

print("comp_turn_codes is:  ", comp_turn_codes)
print("\nAll position combinations of non-zero elements where the elements sum to 2 (mod 4):  ")
print (two_mod_4_combs)


sum_of_2s = []
for two_mod_4_comb in two_mod_4_combs:
	sum_of_2 = []
	for i in range (0, len(comp_turn_codes)):
		if i in two_mod_4_comb:
			sum_of_2.append(comp_turn_codes[i])
		else: sum_of_2.append(0)
	sum_of_2s.append(sum_of_2)


print("\nsum_of_2s  (a.k.a. Every possible useful modification of comp_code_turns. Elements that sum to 2 (mod 4) remain, and the rest are replaced by zeros):  ")
print(sum_of_2s)

print("\nNumber of new algs to generate:  ", len(sum_of_2s), "\n")


#########
#########
#########
import datetime
x = datetime.datetime.now()
print("ZZ_Results_" + x.strftime("%a") + "_" + x.strftime("%f"))

import copy
list1 = [8, 9]
list2 = copy.deepcopy(list1)
