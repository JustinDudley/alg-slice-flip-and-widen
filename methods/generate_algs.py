
import copy

from methods.comp_Xpansion import comp_Xpansion
from methods.get_combos import get_combos
from methods.insert_merge_YU_algs import insert_merge_YU_algs
from methods.helper_methods import get_single_rotation_code
from variables.constants import AXIS_FAMILY
from variables.dataframes import df_Ripple_L


def generate_algs(listTypeAlg:list[str], trailing_YorZ_Xs_dual):

    from_single_SS__rippled_and_expanded_strTypeAlgs:list[str] = []
    for trailing_YorZ_Xs in trailing_YorZ_Xs_dual:

        print("trailing_YorZ_Xs[0] is: ", trailing_YorZ_Xs[0])


        add_YorZ__shifting_listTypeAlg = copy.deepcopy(listTypeAlg)
        add_YorZ__shifting_listTypeAlg.append(trailing_YorZ_Xs[0])

        
        #   +1  because alg_turns_plus_YorZ_shifting has ONE MORE TURN then alg_turns: The YorZ component (eg. Y',  Z2...).  But I don't want to iterate over a shifting list.
        for indx in reversed(range(len(listTypeAlg) + 1)):

            alg_rotation_codes = copy.deepcopy(list(map(get_single_rotation_code, add_YorZ__shifting_listTypeAlg)))
            print("\n\n\n\n\n\n\nposition of the turn the YorZ is currently next to (not sure, right now, which side!): ", indx)
            print("\nrotation_codes, specific to the turn the YorZ is next to: ", alg_rotation_codes)
            DNA_3_marker_cums = get_combos(alg_rotation_codes, trailing_YorZ_Xs)
            print("\nalg + WCR before iterating: ", " ".join(add_YorZ__shifting_listTypeAlg), " __ + __ ", trailing_YorZ_Xs[1], "\n")

            
            if indx == 0:           # this will be true only on the very last iteration
                one_round_of__final_strTypeAlgs = comp_Xpansion(add_YorZ__shifting_listTypeAlg, DNA_3_marker_cums)
                from_single_SS__rippled_and_expanded_strTypeAlgs.extend(one_round_of__final_strTypeAlgs)
                break
            
            # alg_turns_plus_YorZ_shifting will have its turns replaced one by one from the right. indx - 1 should always be ONE step ahead of this shift, so it should give an accurate turn
            # to avoid generating duplicates.  U Y is equivalent to Y U, so we're going to pass over U Y and only examine Y U 
            elif AXIS_FAMILY[add_YorZ__shifting_listTypeAlg[indx - 1]] != AXIS_FAMILY[trailing_YorZ_Xs[0]]:  
                one_round_of__final_strTypeAlgs = comp_Xpansion(add_YorZ__shifting_listTypeAlg, DNA_3_marker_cums)
                for alg in one_round_of__final_strTypeAlgs:
                    print(alg)
                from_single_SS__rippled_and_expanded_strTypeAlgs.extend(one_round_of__final_strTypeAlgs)
                if trailing_YorZ_Xs[0] == "Y0" or trailing_YorZ_Xs[0] == "Z0":
                    break    # avoid creating duplicates. No need to ripple a zero-effect turn through and keep doing comp_Xpansion. By including the break HERE, a Y0 (or Z0) may ripple in a couple times, if the alg ends with U or U D.  I can live with that. There will still only be one Xpansion performed.  


            #  RIPPLE LEFT one time
            #  these two lines swap two elements of the list.  The YorZ component is always one of the two. It is rippling through.  
            #  note that, by design, the code only reaches the following lines if indx > 0
            add_YorZ__shifting_listTypeAlg[indx] = df_Ripple_L.at[add_YorZ__shifting_listTypeAlg[indx - 1], "A%s-->%sB"%(trailing_YorZ_Xs[0], trailing_YorZ_Xs[0])]
            add_YorZ__shifting_listTypeAlg[indx - 1] = trailing_YorZ_Xs[0]
    
    from_single_SS__final_strTypeAlgs = insert_merge_YU_algs(from_single_SS__rippled_and_expanded_strTypeAlgs)
            
    return from_single_SS__final_strTypeAlgs
        

