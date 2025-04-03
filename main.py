
import datetime

from variables.constants import GROUP_DICT, GROUP_DIVINER
from methods.helper_methods import compoundify_comp_slice_turns
from methods.sub_in_slices_and_ripple_right import sub_in_slices_and_ripple_right
from methods.generate_algs import generate_algs
from methods.find_pattern import find_pattern


# naming convention:
# turn   ==  a string. one turn in an algorithm
# turns  ==  a list. An alg whose turns are members of a list
# alg    ==  an alg that is a string
# als    ==  a list of algs that are strings    


# Note on TESTING: There are 3 lines of code that invoke the testing methods TESTING_1, TESTING_2, TESTING_3.
# see testing/README__...
# These methods simply add a few explanatory notes to the list of algs that will be written to file
# To add the notes:  Set is_test to TRUE in the file called testing/is_test



startTime = datetime.datetime.now() # to monitor performance of program

with open("/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/INPUT_file/alg_list_StickerSolve_input.txt") as file_input:
    stic_algs = file_input.read().splitlines() 




all__final_algs = []
for stic_alg in stic_algs:

	# FIND GROUP NUMBER
	pattern = find_pattern(stic_alg)
	group_number = GROUP_DIVINER[pattern[7]]  # pattern[7] gives the sticker at Corner_Location_B


	#  U D' --> UD'
	stic_alg_compoundified = compoundify_comp_slice_turns(stic_alg)    # For instance:   U R2 UD' F B L' B2 R UD' B RL' U2 B2
	stic_turns = stic_alg_compoundified.split()
	trailing_WCRs = GROUP_DICT[group_number]  # no need for dual CoRo schemes here 



	# SLICE/RIPPLE_R
	motley_list = sub_in_slices_and_ripple_right(stic_turns, trailing_WCRs)
	stic_turns = motley_list[0]
	trailing_YorZ_Xs_dual:list[list[str]] = motley_list[1]



	# GENERATE ALGS
	single_stic_origin__final_algs = generate_algs(stic_turns, trailing_YorZ_Xs_dual, stic_alg)
	all__final_algs.extend(single_stic_origin__final_algs)





# WRITE TO FILE
dt = datetime.datetime.now()
output_filename = '/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/OUTPUT_files/%s.txt'%(dt.strftime("%a") + "_" + dt.strftime("%I") + ":" + dt.strftime("%M") + ":" + dt.strftime("%S") + "_output")
with open(output_filename, "x") as output_file:
	for alg in all__final_algs:  # write all of one base alg's final algs to file. If my testing methods are uncommented, ripple-round-specific info will get baked in to the list of final algs. It will look like I've written to file several times, but I haven't. The PYTHON LIST ITSELF just includes carriage returns and explanations when is_test is set to True
		output_file.write(f"{alg}\n")



print("time elapsed: ", datetime.datetime.now() - startTime)
