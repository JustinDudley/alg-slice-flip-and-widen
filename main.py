
import pandas as pd 
from variables import *  
from methods import *
from sub_in_slices_and_ripple_right import *
from generate_algs import *


# print("\n\ndf_complements_and_inverses:\n\n", df_complements_and_inverses, "\n")
# print("df_Ripple_R:\n\n", df_Ripple_L, "\n")
# print("df_Ripple_L:\n\n", df_Ripple_R, "\n")

# print("df_stickers_turned:\n\n", df_stickers_turned, "\n")
# print("df_stickers_rotated:\n\n", df_stickers_rotated, "\n")
# print("df_stickers_reflected:\n\n", df_stickers_reflected, "\n")



group_number = 6    # Must choose a group before running program. (1-6)
alg = "U2 L F B' U' R2 L B' U2 F U' D R' U2 L B'"
# alg = "U R2 U D' F B L' B2 R U D' B R L' U2 B2"  ,  group 1


# 1.  1.  1.  1.  1.  
# # I will read a .txt file to get the StickerSolve alg strings at this point and put it into a list (or possibly read an excel file, but that seems like over-doing it)
# The first loop will begin HERE:
# for StickerSolve_string in StickerSolve_strings:
	# condense the alg string, then convert string to a list, name it alg_turns. 


alg = condense_comp_slice_turns(alg)    # For instance:   U R2 UD' F B L' B2 R UD' B RL' U2 B2
alg_turns = alg.split()
#it's good that I'm re-setting trailing_WCRs INSIDE the first loop, since trailing_WCRs will get changed in the code that follows
trailing_WCRs = GROUP_DICT[group_number]  # NOTe! At this point, there is no need for dual CoRo schemes or for any standardized way of writing the CoRo. They will all crunch down the same 


# SLICE/RIPPLE_R
motley_list = sub_in_slices_and_ripple_right(alg_turns, trailing_WCRs)
alg_turns = motley_list[0]
trailing_WCRs_dual = motley_list[1]



print("alg_turns after sub in slices and ripple right: ", alg_turns)
print("trailing_WCRs_dual after sub in slices and ripple right: ", trailing_WCRs_dual)
print("\n")
# I haven't yet chanced upon an alg that yielded a dual WCR, so I should keep testing to make sure that works okay



final_algs_pipe_string = generate_algs(alg_turns, trailing_WCRs_dual)
print(final_algs_pipe_string)





#########
#########
#########
import datetime
x = datetime.datetime.now()
print("ZZ_Results_" + x.strftime("%a") + "_" + x.strftime("%f"))

import copy
list1 = [8, 9]
list2 = copy.deepcopy(list1)
