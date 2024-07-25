
import copy

from testing.is_test import is_test
from methods.comp_Xpansion import comp_Xpansion
from methods.itertools_get_combos import itertools_get_combos
from methods.insert_merge_YU_algs import insert_merge_YU_algs
from methods.helper_methods import get_single_turn_code
from variables.constants import AXIS_FAMILY
from variables.dataframes import df_Ripple_L
from testing.extend__write_to_file import TESTING_2, TESTING_3, TESTING_1


def generate_algs(listTypeAlg:list[str], trailing_YorZ_Xs_dual, strTypeAlg):


    ALL_ripple_rounds_from_single_SS__strTypeAlgs:list[str] = []
    if is_test: ALL_ripple_rounds_from_single_SS__strTypeAlgs = TESTING_1(ALL_ripple_rounds_from_single_SS__strTypeAlgs, strTypeAlg, listTypeAlg)


    for trailing_YorZ_Xs in trailing_YorZ_Xs_dual:
        if is_test: ALL_ripple_rounds_from_single_SS__strTypeAlgs = TESTING_2(ALL_ripple_rounds_from_single_SS__strTypeAlgs, trailing_YorZ_Xs_dual, trailing_YorZ_Xs)
        add_YorZ__shifting_listTypeAlg = copy.deepcopy(listTypeAlg)
        add_YorZ__shifting_listTypeAlg.append(trailing_YorZ_Xs[0])


        for indx in reversed(range(len(listTypeAlg) + 1)):   #   +1 because of the extra YorZ item. Don't want to use add_YorZ__shifting_listTypeAlg for this because it is changing.
            # alg_turns_plus_YorZ_shifting will have its turns replaced one by one from the right. indx - 1 should always be ONE step ahead of this shift, so it should give an accurate turn
            # to avoid generating duplicates.  U Y is functionally equivalent to Y U, so we're going to pass over U Y and only examine Y U 
            if indx == 0 or AXIS_FAMILY[add_YorZ__shifting_listTypeAlg[indx - 1]] != AXIS_FAMILY[trailing_YorZ_Xs[0]]:
                alg_turn_codes = copy.deepcopy(list(map(get_single_turn_code, add_YorZ__shifting_listTypeAlg)))
                DNA_3_marker_cums = itertools_get_combos(alg_turn_codes, trailing_YorZ_Xs)
                one_ripple_round_of__final_strTypeAlgs = comp_Xpansion(add_YorZ__shifting_listTypeAlg, DNA_3_marker_cums)
                if trailing_YorZ_Xs[1] == "X0": one_ripple_round_of__final_strTypeAlgs = [" ".join(add_YorZ__shifting_listTypeAlg)] + one_ripple_round_of__final_strTypeAlgs  # The final touch!!  When an alg ends up with an X0 due to slice substitution, THE ALG ITSELF must be added to the list of finals WITHOUT ANY COMP SUBSTITUTION. My intricate CompXpansion logic with its search for combos looks ONLY for comp opportunites. These algs are overlooked because they are already in a FINAL state WITHOUT COMP SUBSTITUTION!  So they must be appended here.
                one_ripple_round_of__final_strTypeAlgs = insert_merge_YU_algs(one_ripple_round_of__final_strTypeAlgs)
                
                if is_test: one_ripple_round_of__final_strTypeAlgs = TESTING_3(one_ripple_round_of__final_strTypeAlgs, indx, add_YorZ__shifting_listTypeAlg)
                ALL_ripple_rounds_from_single_SS__strTypeAlgs.extend(one_ripple_round_of__final_strTypeAlgs)
            

                if trailing_YorZ_Xs[0] == "Y0" or trailing_YorZ_Xs[0] == "Z0":
                    break    # avoid creating duplicates. No need to ripple a zero-effect turn through and keep doing comp_Xpansion. By including the break HERE, a Y0 (or Z0) may ripple in a couple times, if the alg ends with U or U D.  I can live with that. There will still only be one Xpansion performed.  
                if indx == 0:
                    break  


            #  RIPPLE LEFT one time          These two lines swap two elements of the list.  The YorZ component is always one of the two. It is rippling through.  
            add_YorZ__shifting_listTypeAlg[indx] = df_Ripple_L.at[add_YorZ__shifting_listTypeAlg[indx - 1], "A%s-->%sB"%(trailing_YorZ_Xs[0], trailing_YorZ_Xs[0])]
            add_YorZ__shifting_listTypeAlg[indx - 1] = trailing_YorZ_Xs[0]
    
       
       
    return ALL_ripple_rounds_from_single_SS__strTypeAlgs
        