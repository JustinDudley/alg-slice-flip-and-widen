
import datetime
import copy

from methods.discard_most_algs import discard_most_algs
from methods.find_reversible_index_if_any__build_master_dict import find_reversible_index_if_any__build_master_dict
from methods.reversify_selected_algs__build_stic_alg_dict import reversify_selected_algs__build_stic_alg_dict
from variables.constants import GROUP_DICT, GROUP_DIVINER
from methods.compoundify_comp_slice_turns import compoundify_comp_slice_turns
from methods.sub_in_slices_and_ripple_right import sub_in_slices_and_ripple_right
from methods.generate_algs import generate_algs
from methods.find_pattern import find_pattern


# naming conventions:
# turn   ==  a string. one turn in an algorithm
# turns  ==  a list. An alg whose turns are members of a list
# alg    ==  an alg that is a string
# als    ==  a list of algs that are strings    


# Note on TESTING: There are 3 lines of code that invoke the testing methods TESTING_1, TESTING_2, TESTING_3.
# see testing/README__...
# These methods simply add a few explanatory notes to the list of algs that will be written to file
# To add the notes:  Set is_test to TRUE in the file called testing/is_test


# 3 main alg-containing structures in this project (2 lists and 1 dictionary):
#    stic_algs        -- a list of strings. Each string is a Sticker Solve algorithm from in input file
#    stic_alg_dicts   -- a list of dictionaries. For Sticker Solve algs that have a tri-turn reversal opportunity, a new alg is appended to the original list. Then, immediately, each alg in the list (original and reversified) is put into a dictionary. Each dictionary has (1) a Sticker Solve algorithm or a Sticker Solve algorithm's reversified counterpart, and (2) a boolean indicating whether the alg is a reversified alg.
#    stic_master_dict  -- There is one stic_master_dict for every stic_algs_dict, but stic_master_dict lives within a loop and never becomes collected into a LIST of dictionaries. Each stic_master_dict has (1) the TURNS of a Sticker Solve algorithm with slices now subbed in (or a reversified alg with slices now subbed in) so the alg is now in the form of a LIST OF TURNS, and is no longer a string,  (2) the original souce alg, IN ITS ORIGINAL PRE-SLICE FORM, SO IT COULD INCLUDE "R' L" INSTEAD OF "T", FOR INSTANCE, (3) a boolean indicating whether the alg is a reversified alg, and (4) the index of the LIST ITEM that is the first of the two list items in the reversified pair, if the turns list is the result of a pair swap. (index =  -1 if the turns list in question is not the result of a swapping)





startTime = datetime.datetime.now() # to monitor performance of program

with open("/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/INPUT_file/alg_list_StickerSolve_input.txt") as file_input:
    stic_algs = file_input.read().splitlines() 

# Create a list of dictionaries.
stic_alg_dicts = reversify_selected_algs__build_stic_alg_dict(stic_algs)





all__final_algs = []
for stic_alg_dict in stic_alg_dicts:

	# FIND GROUP NUMBER
	pattern = find_pattern(stic_alg_dict["alg"])
	group_number = GROUP_DIVINER[pattern[7]]  # pattern[7] gives the sticker at Corner_Location_B


	# COMPOUNDIFY   U D' --> UD'
	stic_alg_compoundified = compoundify_comp_slice_turns(stic_alg_dict["alg"])    # For instance:   U R2 UD' F B L' B2 R UD' B RL' U2 B2
	stic_turns = copy.deepcopy(stic_alg_compoundified.split())
	# no need for dual CoRo schemes in line below
	trailing_WCRs = copy.deepcopy(GROUP_DICT[group_number])  # See repeat of this line below.  After 8 hours of fighting with scope, and never understanding why changes within "sub_in_slices_and_ripple_right" change the value of trailing_WCRs here in main AND the value of GROUP_DICT[group_number]  **NO, THAT'S NOT A TYPO!** this is the only workaround I can come up with to make trailing_WCRs behave as I believe it should. I am utterly baffled. 

	
	for leading_X in ["X", "X'", "X2"]:

		# SLICE/RIPPLE_R
		# sub_in_slices_and_ripple_right contains the MEAT of the NEW FUNCTIONALITY of this leading_X branch
		# note the destructuring syntax below
		stic_turns = copy.deepcopy(stic_alg_compoundified.split())    # I am in scope hell. I feel like this is my first day of learning Python... and I'm not getting it
		stic_turns, trailing_YorZ_Xs_dual = sub_in_slices_and_ripple_right(stic_turns, trailing_WCRs, leading_X)
		trailing_WCRs = copy.deepcopy(GROUP_DICT[group_number])  # See repeat of this line above.  After 8 hours of fighting with scope, and never understanding why changes within "sub_in_slices_and_ripple_right" change the value of trailing_WCRs here in main AND the value of GROUP_DICT[group_number]  **NO, THAT'S NOT A TYPO!** this is the only workaround I can come up with to make trailing_WCRs behave as I believe it should. I am utterly baffled. 
		

		# SET INDEX IN THE CASE OF A REVERSIBLE TRI-TURN, and BUILD A MASTER DICTIONARY that includes (1) TURNS (alg in list form), (2) the ORIGINAL ALG BEFORE SLICES SUBBED IN, (3) a boolean called IS_REVERSIFIED, and (4) the index of the first TURN of the two tri-turns in the list called "turns" (If an alg is not reversified the index is set to -1)
		stic_master_dict = find_reversible_index_if_any__build_master_dict(stic_turns, stic_alg_dict)


		# GENERATE ALGS
		single_stic_origin__final_algs = generate_algs(stic_master_dict, trailing_YorZ_Xs_dual)


		# ADD LEADING_X TO EACH ALG;  ADD GROUP OF ALGS TO TOTAL GROUP OF ALGS
		for i in range(len(single_stic_origin__final_algs)):
			single_stic_origin__final_algs[i] = leading_X + " " + single_stic_origin__final_algs[i]
		all__final_algs.extend(single_stic_origin__final_algs)



all__final_algs = discard_most_algs(all__final_algs)




# WRITE TO FILE
dt = datetime.datetime.now()
output_filename = '/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/OUTPUT_files/%s.txt'%(dt.strftime("%a") + "_" + dt.strftime("%I") + ":" + dt.strftime("%M") + ":" + dt.strftime("%S") + "_output")
with open(output_filename, "x") as output_file:
	for alg in all__final_algs:  # write all of one base alg's final algs to file. If my testing methods are uncommented, ripple-round-specific info will get baked in to the list of final algs. It will look like I've written to file several times, but I haven't. The PYTHON LIST ITSELF just includes carriage returns and explanations when is_test is set to True
		output_file.write(f"{alg}\n")



print("time elapsed: ", datetime.datetime.now() - startTime)
