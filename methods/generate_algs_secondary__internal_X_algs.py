

import copy
from methods.comp_Xpansion import comp_Xpansion
from methods.get_single_turn_code import get_single_turn_code
from methods.itertools_get_combos import itertools_get_combos
from variables.constants import AXIS_FAMILY, INTERNAL_X_INVERSE_DICT, MERGE_YU_DICT, WHAT_BRINGS_U_HERE
from variables.dataframes import df_stickers_turned, df_Ripple_L, df_turn_attributes, df_Ripple_R


def move_sticker_once__X_file_version(sticker, WCR):
	return df_stickers_turned.at[sticker, WCR]


# The sister method to this one, in another file, returnes a LIST of LIST of string.  This one here only returns a STRING (TWO levels lower)
def replace_two_Trailing_Xs_with_a_single_X(Trailing_X_WCRs):
	sticker = "U"
	for Trailing_X_WCR in Trailing_X_WCRs:
		sticker = move_sticker_once__X_file_version(sticker, Trailing_X_WCR)
	combined_X = WHAT_BRINGS_U_HERE[sticker]
	return combined_X



def generate_algs_secondary__internal_X_algs(alg_of_udfb_friendly_turns, trailing_X_by_itself):

    ALL_ripple_rounds__within_parent_methods_SINGLE_ripple_round__final_algs = []
    for internal_X_turn, internal_X_inverse in INTERNAL_X_INVERSE_DICT.items():   # key, value syntax.  KEY: X_turn,  VALUE: X_WCR_inverse
        
       # STEP ONE: CREATE Merge_YU ALG (udfb ALG), ESTABLISH THE WCR'S in TRAILING_X_Xs
        alg = " ".join(alg_of_udfb_friendly_turns)
        alg = alg + " "     # so that the search ("if key in alg") works even for turns that aren't counterclockwise or double

        alg_turns = [] 
        alg_contains_YU = False
        for key, value in MERGE_YU_DICT.items():   
            if key in alg:                 # because don't want to append again if no change
                alg_contains_YU = True
                alg = alg.replace(key, value)
                alg = alg.strip()
                alg_turns = list(alg.strip().split(" "))
        if not alg_contains_YU:
            continue  
        
        # only an alg that has a newly swapped-in udfb will get to this point of the method
        second_and_third_trailing_Xs = [internal_X_inverse, trailing_X_by_itself]  #example:  S D' U' L D U B' R2 D2 F' R L U F2 R2 d R2  'X'  (the 'X' is "trailiing_X_by_itself").   This alg gets an identity element added to it near the end, becoming  S D' U' L D U B' R2 D2 F' R L U F2 R2 d R2  {X X'} 'X'.  Of those 3 confusing X's at the end of that alg:  The first will ripple through. The second and third will be combined and called "combined_X", and become the basis for what itertools gets set to 
        combined_X__second_and_third = replace_two_Trailing_Xs_with_a_single_X(second_and_third_trailing_Xs)
        trailing_X_Xs = [internal_X_turn, combined_X__second_and_third]   # This makes the notation in this file consistent with the trailing_YorZ_Xs notation and concept




        # STEP TWO:  RIPPLE the X, DO ITERTOOLS, GENERATE ALGS
        X_added__shifting_turns = copy.deepcopy(alg_turns)
        X_added__shifting_turns.append(trailing_X_Xs[0])

        for indx in reversed(range(len(alg_turns) + 1)):   #   +1 because of the extra X item.   # X_added__shifting_turns will have its turns replaced one by one from the right. indx - 1 should always be ONE step ahead of this shift, so it should give an accurate turn
            if indx < len(alg_turns) and indx > 0 and AXIS_FAMILY[X_added__shifting_turns[indx - 1]] != AXIS_FAMILY[trailing_X_Xs[0]] and AXIS_FAMILY[X_added__shifting_turns[indx + 1]] != AXIS_FAMILY[trailing_X_Xs[0]]:  # Don't want trailing X, don't want leading X, don't want any type of R/L/T turn either before OR after the internal X

                turn_codes = copy.deepcopy(list(map(get_single_turn_code, X_added__shifting_turns)))
                DNA_3_marker_cums = itertools_get_combos(turn_codes, trailing_X_Xs)
                one_ripple_round_of__final_algs = comp_Xpansion(X_added__shifting_turns, DNA_3_marker_cums)
                if trailing_X_Xs[1] == "X0": one_ripple_round_of__final_algs = [" ".join(X_added__shifting_turns)] + [" "] + one_ripple_round_of__final_algs  # The final touch!!  When an alg ends up with an X0 due to slice substitution, THE ALG ITSELF must be added to the list of finals WITHOUT ANY COMP SUBSTITUTION. My intricate CompXpansion logic with its search for combos looks ONLY for comp opportunites. These algs are overlooked because they are already in a FINAL state WITHOUT COMP SUBSTITUTION!  So they must be appended here.
                if trailing_X_Xs[1] == "X0": one_ripple_round_of__final_algs.remove(" ") # probably harmless?
           
                ALL_ripple_rounds__within_parent_methods_SINGLE_ripple_round__final_algs.extend(one_ripple_round_of__final_algs)
                
                if indx == 0:
                    break  


            #  RIPPLE LEFT one time          These two lines swap two elements of the list.  The YorZ component (in THIS branch the first X component) is always one of the two. It is rippling through.  
            X_added__shifting_turns[indx] = df_Ripple_L.at[X_added__shifting_turns[indx - 1], "A%s-->%sB"%(trailing_X_Xs[0], trailing_X_Xs[0])]
            X_added__shifting_turns[indx - 1] = trailing_X_Xs[0]


    return ALL_ripple_rounds__within_parent_methods_SINGLE_ripple_round__final_algs
