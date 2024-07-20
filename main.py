
import datetime

from variables.constants import GROUP_DICT, CODE, GROUP_DIVINER
from methods.helper_methods import compoundify_comp_slice_turns
from methods.sub_in_slices_and_ripple_right import sub_in_slices_and_ripple_right
from methods.generate_algs import generate_algs
from methods.find_pattern import find_pattern

# naming convention:
# 
# turn        ==  a string.  one turn in an algorithm
# listTypeAlg  ==  a list.  an algorithm whose turns are members of a list.  2 examples:  (1) LstTypeAlg, (2) static_LstTypeAlg
# strTypeAlg  ==  a string. an algorithm whose turns are part of a single long string.
# strTypeAlgs ==  a list of strings. A list whose members are StrTypeAlg        



# TO-DO:  See line 39, sub_in_slices_and_ripple_right:
# What happens if slice_opportunity_positions is empty?  Do I need to account for this?




# NOTE:  it IS possible for an SS_alg to produce ZERO results. For instance:  group 2, "U' F' B2 D R L' U F' D' L' F' B R' B' R D2"


strTypeAlg = "F2 U' B' L' F D' F U' R2 U R' U' R2 D2 R' F L'"
# get the pattern JUST FOR THE FIRST alg in the list
pattern = find_pattern(strTypeAlg)
# get the group_number JUST FROM THE FIRST alg in the list
group_number = GROUP_DIVINER[pattern[7]]  # pattern[7] gives the sticker at Corner_Location_B



# read StickerSolve algs from .txt file, put into List 
# First loop begins HERE:
# for SticSolv_alg in SticSolv_algs:
	# etc.


all_final_strTypeAlgs:list[str] = []



strTypeAlg = compoundify_comp_slice_turns(strTypeAlg)    # For instance:   U R2 UD' F B L' B2 R UD' B RL' U2 B2
listTypeAlg = strTypeAlg.split()
trailing_WCRs = GROUP_DICT[group_number]  # no need for dual CoRo schemes here 


# SLICE/RIPPLE_R
motley_list = sub_in_slices_and_ripple_right(listTypeAlg, trailing_WCRs)
listTypeAlg:list[str] = motley_list[0]
trailing_YorZ_Xs_dual:list[list[str]] = motley_list[1]


# I haven't yet chanced upon an alg that yielded a dual WCR, so I should keep testing to make sure that works okay



from_single_SS__final_strTypeAlgs = generate_algs(listTypeAlg, trailing_YorZ_Xs_dual)
for final_alg in from_single_SS__final_strTypeAlgs:
    all_final_strTypeAlgs.append(final_alg)


# print("\nall_final_strTypeAlgs is:  ")
# for final_alg in all_final_strTypeAlgs:
#     print(final_alg)




x = datetime.datetime.now()
filename = '/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/OUTPUT_files/output_%s.txt'%(x.strftime("%a") + "_" + x.strftime("%I") + ":" + x.strftime("%M") + ":" + x.strftime("%S"))
with open(filename, 'w') as output_file:
	output_file.write(f"** ALL ALGS:\n\n")
	output_file.write(f"alg after slice insertion is:  {" ".join(listTypeAlg)}\n")
	for alg in all_final_strTypeAlgs:
		output_file.write(f"{alg}\n")

