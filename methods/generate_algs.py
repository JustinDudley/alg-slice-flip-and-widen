
import copy

from methods.comp_Xpansion import comp_Xpansion
from methods.get_combos import get_combos
from methods.helper_methods import get_single_rotation_code
from variables.constants import AXIS_MEMBERSHIP
from variables.dataframes import df_Ripple_L


def generate_algs(alg_turns:list[str], trailing_YorZ_Xs_dual):

    final_algs_from_single_SticSolv:list[str] = []
    for trailing_YorZ_Xs in trailing_YorZ_Xs_dual:

        print("trailing_YorZ_Xs[0] is: ", trailing_YorZ_Xs[0])


        alg_turns_plus_YorZ_shifting = copy.deepcopy(alg_turns)
        alg_turns_plus_YorZ_shifting.append(trailing_YorZ_Xs[0])

        
        #   +1  because alg_turns_plus_YorZ_shifting has ONE MORE TURN then alg_turns: The YorZ component (eg. Y',  Z2...).  But I don't want to iterate over a shifting list.
        for indx in reversed(range(len(alg_turns) + 1)):

            rotation_codes = copy.deepcopy(list(map(get_single_rotation_code, alg_turns_plus_YorZ_shifting)))
            DNA_3_marker_cums = get_combos(rotation_codes, trailing_YorZ_Xs)
            print(indx, "\n -- ", " ".join(alg_turns_plus_YorZ_shifting), " -- ", trailing_YorZ_Xs[1])
            print("rotation_codes: ", rotation_codes, "\n")

            
            if indx == 0:           # this will be true only the very last iteration
                one_round_of_final_algs = comp_Xpansion(alg_turns_plus_YorZ_shifting, DNA_3_marker_cums)
                final_algs_from_single_SticSolv.extend(one_round_of_final_algs)
                break
            
            # alg_turns_plus_YorZ_shifting will have its turns replaced one by one from the right. indx - 1 should always be ONE step ahead of this shift, so it should give an accurate turn
            # to avoid generating duplicates.  U Y is equivalent to Y U, so we're going to pass over U Y and only examine Y U 
            elif AXIS_MEMBERSHIP[alg_turns_plus_YorZ_shifting[indx - 1]] != AXIS_MEMBERSHIP[trailing_YorZ_Xs[0]]:  
                # do I need to initialize one_round previously if I'm going to reference it twice like this?
                one_round_of_final_algs = comp_Xpansion(alg_turns_plus_YorZ_shifting, DNA_3_marker_cums)
                for alg in one_round_of_final_algs:
                    print(alg)
                final_algs_from_single_SticSolv.extend(one_round_of_final_algs)
                if trailing_YorZ_Xs[0] == "Y0" or trailing_YorZ_Xs[0] == "Z0":
                    break    # avoid creating duplicates. No need to ripple a zero-effect turn through and keep doing comp_Xpansion. By including the break HERE, a Y0 (or Z0) may ripple in a couple times, if the alg ends with U or U D.  I can live with that. There will still only be one Xpansion performed.  


            #  RIPPLE LEFT one time
            #  these two lines swap two elements of the list.  The YorZ component is always one of the two. It is rippling through.  
            #  note that, by design, the code only reaches the following lines if indx > 0
            alg_turns_plus_YorZ_shifting[indx] = df_Ripple_L.at[alg_turns_plus_YorZ_shifting[indx - 1], "A%s-->%sB"%(trailing_YorZ_Xs[0], trailing_YorZ_Xs[0])]
            alg_turns_plus_YorZ_shifting[indx - 1] = trailing_YorZ_Xs[0]
    
            
    return final_algs_from_single_SticSolv
        

