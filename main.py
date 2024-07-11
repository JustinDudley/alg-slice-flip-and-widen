
import pandas as pd 
from variables.constants import GROUP_DICT
from methods.helper_methods import condense_comp_slice_turns
from methods.sub_in_slices_and_ripple_right import sub_in_slices_and_ripple_right
from methods.generate_algs import generate_algs



group_number = 5    # Must choose a group before running program. (1-6)
SticSolv_alg = "U' L' B L2 F' U' D R F2 L' B R2 L U' D B2"
# This seems to work.  "U2 L F B' U' R2 L B' U2 F U' D R' U2 L B'"    So let's try another one.


final_algs_ALL = []
big_dict = {}  # keys are SS_algs, values are lists (or pipe strings) of result algs
# thinking to write data to excel in TWO ways:  (1) list every SticSolv alg and its own results, (2) listing of ALL algs, broken into sublists like "No B, B', B2"


# read StickerSolve algs from .txt file, put into List 
# First loop begins HERE:
# for SticSolv_alg in SticSolv_algs:
	# etc.




SticSolv_alg = condense_comp_slice_turns(SticSolv_alg)    # For instance:   U R2 UD' F B L' B2 R UD' B RL' U2 B2
alg_turns = SticSolv_alg.split()
trailing_WCRs = GROUP_DICT[group_number]  # no need for dual CoRo schemes here 


# SLICE/RIPPLE_R
motley_list = sub_in_slices_and_ripple_right(alg_turns, trailing_WCRs)
alg_turns:list[str] = motley_list[0]
trailing_YorZ_Xs_dual:list[list[str]] = motley_list[1]



print("alg_turns after sub in slices and ripple right: ", alg_turns)
print("trailing_WCRs_dual after sub in slices and ripple right: ", trailing_YorZ_Xs_dual, "\n")
# I haven't yet chanced upon an alg that yielded a dual WCR, so I should keep testing to make sure that works okay



final_algs_from_single_SticSolv = generate_algs(alg_turns, trailing_YorZ_Xs_dual)
for final_alg in final_algs_from_single_SticSolv:
    final_algs_ALL.append(final_alg)


print("final_algs_ALL is:  ", final_algs_ALL)


#########
#########
#########
import datetime
x = datetime.datetime.now()
print("ZZ_Results_" + x.strftime("%a") + "_" + x.strftime("%f"))

import copy
list1 = [8, 9]
list2 = copy.deepcopy(list1)
