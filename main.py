
import datetime

from variables.constants import GROUP_DICT, GROUP_DIVINER
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


# Note on TESTING: There are 3 lines of code that call testing methods.
# These methods simply add a few explanatory notes to the list of algs that will be written to file
# The methods are called TESTING_1, TESTING_2, TESTING_3.
# To add the notes:  Set is_test to TRUE in the file testing/is_test



startTime = datetime.datetime.now() # to monitor performance of program

with open("/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/INPUT_file/alg_list_input.txt") as file_input:
    strTypeAlgs = file_input.read().splitlines() 




all_final_strTypeAlgs:list[str] = []
for strTypeAlg in strTypeAlgs:

	pattern = find_pattern(strTypeAlg)
	group_number = GROUP_DIVINER[pattern[7]]  # pattern[7] gives the sticker at Corner_Location_B



	compoundified_strTypeAlg = compoundify_comp_slice_turns(strTypeAlg)    # For instance:   U R2 UD' F B L' B2 R UD' B RL' U2 B2
	listTypeAlg = compoundified_strTypeAlg.split()
	trailing_WCRs = GROUP_DICT[group_number]  # no need for dual CoRo schemes here 



	# SLICE/RIPPLE_R
	motley_list = sub_in_slices_and_ripple_right(listTypeAlg, trailing_WCRs)
	listTypeAlg:list[str] = motley_list[0]
	trailing_YorZ_Xs_dual:list[list[str]] = motley_list[1]



	from_single_SS__final_strTypeAlgs = generate_algs(listTypeAlg, trailing_YorZ_Xs_dual, strTypeAlg)
	all_final_strTypeAlgs.extend(from_single_SS__final_strTypeAlgs)






dt = datetime.datetime.now()
output_filename = '/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/OUTPUT_files/%s.txt'%(dt.strftime("%a") + "_" + dt.strftime("%I") + ":" + dt.strftime("%M") + ":" + dt.strftime("%S") + "_output")
with open(output_filename, "x") as output_file:
	for alg in all_final_strTypeAlgs:  # write all of one base alg's final algs to file. If my testing methods are uncommented, ripple-round-specific info will get baked in to the list of final algs. It will look like I've written to file several times, but I haven't. The PYTHON LIST ITSELF just includes carriage returns and explanations when is_test is set to True
		output_file.write(f"{alg}\n")



print("time elapsed: ", datetime.datetime.now() - startTime)
