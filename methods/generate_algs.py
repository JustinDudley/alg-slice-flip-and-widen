
import copy

from methods.comp_Xpansion import comp_Xpansion
from methods.itertools_get_combos import itertools_get_combos
from methods.insert_merge_YU_algs import insert_merge_YU_algs
from methods.helper_methods import get_single_turn_code
from variables.constants import AXIS_FAMILY
from variables.dataframes import df_Ripple_L
from testing.extend_write_to_file import TESTING_1, TESTING_2


def generate_algs(listTypeAlg:list[str], trailing_YorZ_Xs_dual):

    ALL_ripple_rounds_from_single_SS__strTypeAlgs:list[str] = []
    for trailing_YorZ_Xs in trailing_YorZ_Xs_dual:
        ALL_ripple_rounds_from_single_SS__strTypeAlgs = TESTING_1(ALL_ripple_rounds_from_single_SS__strTypeAlgs, trailing_YorZ_Xs_dual, trailing_YorZ_Xs)
        add_YorZ__shifting_listTypeAlg = copy.deepcopy(listTypeAlg)
        add_YorZ__shifting_listTypeAlg.append(trailing_YorZ_Xs[0])


        for indx in reversed(range(len(listTypeAlg) + 1)):   #   +1  because alg_turns_plus_YorZ_shifting has ONE MORE TURN then alg_turns: The YorZ component (eg. Y',  Z2...).  But I don't want to iterate over a shifting list.
            # alg_turns_plus_YorZ_shifting will have its turns replaced one by one from the right. indx - 1 should always be ONE step ahead of this shift, so it should give an accurate turn
            # to avoid generating duplicates.  U Y is equivalent to Y U, so we're going to pass over U Y and only examine Y U 
            if indx == 0 or AXIS_FAMILY[add_YorZ__shifting_listTypeAlg[indx - 1]] != AXIS_FAMILY[trailing_YorZ_Xs[0]]:
                alg_turn_codes = copy.deepcopy(list(map(get_single_turn_code, add_YorZ__shifting_listTypeAlg)))
                DNA_3_marker_cums = itertools_get_combos(alg_turn_codes, trailing_YorZ_Xs)
                one_ripple_round_of__final_strTypeAlgs = comp_Xpansion(add_YorZ__shifting_listTypeAlg, DNA_3_marker_cums)
                one_ripple_round_of__final_strTypeAlgs = insert_merge_YU_algs(one_ripple_round_of__final_strTypeAlgs)
                
                one_ripple_round_of__final_strTypeAlgs = TESTING_2(one_ripple_round_of__final_strTypeAlgs, indx)
                ALL_ripple_rounds_from_single_SS__strTypeAlgs.extend(one_ripple_round_of__final_strTypeAlgs)
            

                if trailing_YorZ_Xs[0] == "Y0" or trailing_YorZ_Xs[0] == "Z0":
                    break    # avoid creating duplicates. No need to ripple a zero-effect turn through and keep doing comp_Xpansion. By including the break HERE, a Y0 (or Z0) may ripple in a couple times, if the alg ends with U or U D.  I can live with that. There will still only be one Xpansion performed.  
                if indx == 0:
                    break  


            #  RIPPLE LEFT one time          These two lines swap two elements of the list.  The YorZ component is always one of the two. It is rippling through.  
            add_YorZ__shifting_listTypeAlg[indx] = df_Ripple_L.at[add_YorZ__shifting_listTypeAlg[indx - 1], "A%s-->%sB"%(trailing_YorZ_Xs[0], trailing_YorZ_Xs[0])]
            add_YorZ__shifting_listTypeAlg[indx - 1] = trailing_YorZ_Xs[0]
    
       
       
    return ALL_ripple_rounds_from_single_SS__strTypeAlgs
        