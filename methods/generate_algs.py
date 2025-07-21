
import copy

from methods.generate_algs_secondary__internal_X_algs import generate_algs_secondary__internal_X_algs
from testing.is_test import is_test
from methods.comp_Xpansion import comp_Xpansion
from methods.itertools_get_combos import itertools_get_combos
from methods.insert_merge_YU_algs import insert_merge_YU_algs
from methods.insert_reinstated_trailing_YorZ__patch import insert_reinstated_trailing_YorZ__patch
from methods.remove_Y0_and_Z0 import remove_Y0_and_Z0
from methods.get_single_turn_code import get_single_turn_code
from variables.constants import AXIS_FAMILY
from variables.dataframes import df_Ripple_L
from testing.extend__write_to_file import TESTING_2, TESTING_3, TESTING_1


def generate_algs(stic_master_dict, trailing_YorZ_Xs_dual):

    stic_turns = stic_master_dict["turns"]
    ALL_ripple_rounds__final_algs = []
    single_ripple_round_of__internal_X_algs = [] # SPECIFIC TO THIS BRANCH
    several_ripple_rounds_of_internal_X__due_to_several_merge_YUs_per_stic_turns__algs = []  # SPECIFIC TO THIS BRANCH

    if is_test: ALL_ripple_rounds__final_algs = TESTING_1(ALL_ripple_rounds__final_algs, stic_master_dict)


    for trailing_YorZ_Xs in trailing_YorZ_Xs_dual:
        if is_test: ALL_ripple_rounds__final_algs = TESTING_2(ALL_ripple_rounds__final_algs, trailing_YorZ_Xs_dual, trailing_YorZ_Xs)
        YorZ_added__shifting_turns = copy.deepcopy(stic_turns)
        YorZ_added__shifting_turns.append(trailing_YorZ_Xs[0])

        

        for indx in reversed(range(len(stic_turns) + 1)):   #   +1 because of the extra YorZ item.   # alg_turns_plus_YorZ_shifting will have its turns replaced one by one from the right. indx - 1 should always be ONE step ahead of this shift, so it should give an accurate turn
                
            if (not stic_master_dict["is_reversified"]) or (stic_master_dict["is_reversified"] and indx == stic_master_dict["tri_turn_list_index"] + 1 and trailing_YorZ_Xs[0] != "Y0" and trailing_YorZ_Xs[0] != "Z0"):      # this is a tragically long OR statement. On the left side of the OR is the normal case where we have a Sticker Solve alg. On the right side is the case where we have a reversified alg. There are a lot of exclusions in place because I don't want to generate a bunch of duplicate results. The only results I want are for the one iteration where the Y or Z element is RIGHT BETWEEN the two reversified turns.  (Also, when the Y or Z is Y0 or Z0, the code would only produce duplicates).    Hmmmm... If a YorZ that is transversing the alg is a "Y" at the moment it bumps into the reversal, and the reversal is currently U D --> D U, the Y is going to bypass both anyway. So... In that case (which WILL happen, right?) the reversified alg just wouldn't generate any final algs at all? That is the if blocks will rule out every iteration? (which is okay)

                if indx == 0 or AXIS_FAMILY[YorZ_added__shifting_turns[indx - 1]] != AXIS_FAMILY[trailing_YorZ_Xs[0]]:    # to avoid generating duplicates.  For instance, U Y (same axis family) is functionally equivalent to Y U, so we're going to pass over U Y, let Y ripple one more to the left, and then examine Y U.


                    # SPECIFIC TO THIS BRANCH
                    # merge_YU algs (ONLY) are subjected to internal X rippling
                    # Note that a Y can interact with MORE THAN ONE turn to create udfb algs
                    # So the following method could be called SEVERAL time on different ripples of the Y, for a single source alg
                    single_ripple_round_of__internal_X_algs = generate_algs_secondary__internal_X_algs(YorZ_added__shifting_turns, trailing_YorZ_Xs[1])
                    several_ripple_rounds_of_internal_X__due_to_several_merge_YUs_per_stic_turns__algs.extend(single_ripple_round_of__internal_X_algs)
                    # SPECIFIC TO THIS BRANCH



                    # in THIS branch, EVERY BIT OF ITERTOOLS FUNCTIONALITY IN THIS METHOD IS COMMENTED OUT BELOW!
                    # THIS METHOD SERVES TO RIPPLE Y OR Z THROUGH THE ALGS, AND FIND merge_YU algs
                    # Then the generate_algs_secondary method is called, and itertools is used THERE as
                    # we ripple X through the algs

                    # turn_codes = copy.deepcopy(list(map(get_single_turn_code, YorZ_added__shifting_turns)))
                    # DNA_3_marker_cums = itertools_get_combos(turn_codes, trailing_YorZ_Xs)
                    # one_ripple_round_of__final_algs = comp_Xpansion(YorZ_added__shifting_turns, DNA_3_marker_cums)
                    # if trailing_YorZ_Xs[1] == "X0": one_ripple_round_of__final_algs = [" ".join(YorZ_added__shifting_turns)] + [" "] + one_ripple_round_of__final_algs  # The final touch!!  When an alg ends up with an X0 due to slice substitution, THE ALG ITSELF must be added to the list of finals WITHOUT ANY COMP SUBSTITUTION. My intricate CompXpansion logic with its search for combos looks ONLY for comp opportunites. These algs are overlooked because they are already in a FINAL state WITHOUT COMP SUBSTITUTION!  So they must be appended here.
                    # one_ripple_round_of__final_algs = insert_merge_YU_algs(one_ripple_round_of__final_algs)
                    # one_ripple_round_of__final_algs = insert_reinstated_trailing_YorZ__patch(one_ripple_round_of__final_algs)
                    
                    # if is_test: one_ripple_round_of__final_algs = TESTING_3(one_ripple_round_of__final_algs, indx, YorZ_added__shifting_turns)
                    # if not is_test and trailing_YorZ_Xs[1] == "X0": one_ripple_round_of__final_algs.remove(" ")
                    # one_ripple_round_of__final_algs = remove_Y0_and_Z0(one_ripple_round_of__final_algs)
                    # ALL_ripple_rounds__final_algs.extend(one_ripple_round_of__final_algs)
                    

                    if trailing_YorZ_Xs[0] == "Y0" or trailing_YorZ_Xs[0] == "Z0":
                        break    # avoid creating duplicates. No need to ripple a zero-effect turn through and keep doing comp_Xpansion. By including the break HERE, a Y0 (or Z0) may ripple in a couple times, if the alg ends with U or U D.  I can live with that. There will still only be one Xpansion performed.  
                    if indx == 0:
                        break  


            #  RIPPLE LEFT one time          These two lines swap two elements of the list.  The YorZ component is always one of the two. It is rippling through.  
            YorZ_added__shifting_turns[indx] = df_Ripple_L.at[YorZ_added__shifting_turns[indx - 1], "A%s-->%sB"%(trailing_YorZ_Xs[0], trailing_YorZ_Xs[0])]
            YorZ_added__shifting_turns[indx - 1] = trailing_YorZ_Xs[0]
    
       
    # ALL_ripple_rounds__final_algs is an empty list, but I'm returning it for old time's sake
    return [ALL_ripple_rounds__final_algs, several_ripple_rounds_of_internal_X__due_to_several_merge_YUs_per_stic_turns__algs]
        