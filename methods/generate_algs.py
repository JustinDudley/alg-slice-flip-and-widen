
import copy

from methods.comp_Xpansion import comp_Xpansion
from methods.get_combos import get_combos
from methods.insert_merge_YU_algs import insert_merge_YU_algs
from methods.helper_methods import get_single_turn_code
from variables.constants import AXIS_FAMILY
from variables.dataframes import df_Ripple_L


def generate_algs(listTypeAlg:list[str], trailing_YorZ_Xs_dual):
    print("NOW INSIDE generate_algs()")

    ALL_ripple_rounds_from_single_SS__strTypeAlgs:list[str] = []

    print("trailing_YorZ_Xs_dual is: ", trailing_YorZ_Xs_dual)
    for trailing_YorZ_Xs in trailing_YorZ_Xs_dual:
    # for trailing_YorZ_Xs in [trailing_YorZ_Xs_dual[0]]:

        print("NOW INSIDE for_trailing_YorZ of potentially TWO trailing_YorZs.  Trailing_YorZ_Xs[0], a.k.a. the YorZ component, is: ", trailing_YorZ_Xs[0])


        add_YorZ__shifting_listTypeAlg = copy.deepcopy(listTypeAlg)
        add_YorZ__shifting_listTypeAlg.append(trailing_YorZ_Xs[0])

        
        #   +1  because alg_turns_plus_YorZ_shifting has ONE MORE TURN then alg_turns: The YorZ component (eg. Y',  Z2...).  But I don't want to iterate over a shifting list.
        for indx in reversed(range(len(listTypeAlg) + 1)):


            alg_turn_codes = copy.deepcopy(list(map(get_single_turn_code, add_YorZ__shifting_listTypeAlg)))
            print("\n\n\n\n\n\n\ncurrent position of the YorZ as it ripples left one turn per loop: ", indx)
            DNA_3_marker_cums = get_combos(alg_turn_codes, trailing_YorZ_Xs)
            print("\nalg + WCR before iterating: ", " ".join(add_YorZ__shifting_listTypeAlg), " __ + __ ", trailing_YorZ_Xs[1], "\n")
           
            #temp solution for when console gets too full:
            # if indx == 13: break
              
            

            if indx == 0:           # this will be true only on the very last iteration
                print("indx is now 0 (zero), ")
                one_ripple_round_of__final_strTypeAlgs = comp_Xpansion(add_YorZ__shifting_listTypeAlg, DNA_3_marker_cums)
                
                # the next line is TEMPORARY. Just for testing:
                one_ripple_round_of__final_strTypeAlgs = ["Going in reverse order, these are the algs for index:", " " + str(indx)] + one_ripple_round_of__final_strTypeAlgs
                ALL_ripple_rounds_from_single_SS__strTypeAlgs.extend(one_ripple_round_of__final_strTypeAlgs)
                
                # PRINT ONE ROUND OF ALGS
                print("Current round of algs:")
                for alg in one_ripple_round_of__final_strTypeAlgs:
                    print(alg)
                    # WHY DOES IT APPEAR THAT SOME ROUNDS AREN'T PRINTING TO CONSOLE???
                
                break
            
            # alg_turns_plus_YorZ_shifting will have its turns replaced one by one from the right. indx - 1 should always be ONE step ahead of this shift, so it should give an accurate turn
            # to avoid generating duplicates.  U Y is equivalent to Y U, so we're going to pass over U Y and only examine Y U 
            elif AXIS_FAMILY[add_YorZ__shifting_listTypeAlg[indx - 1]] != AXIS_FAMILY[trailing_YorZ_Xs[0]]:  
                one_ripple_round_of__final_strTypeAlgs = comp_Xpansion(add_YorZ__shifting_listTypeAlg, DNA_3_marker_cums)
                
                # the next line is TEMPORARY. Just for testing:
                one_ripple_round_of__final_strTypeAlgs = ["\nGoing in reverse order, these are the algs for index:", " " + str(indx)] + one_ripple_round_of__final_strTypeAlgs
                ALL_ripple_rounds_from_single_SS__strTypeAlgs.extend(one_ripple_round_of__final_strTypeAlgs)
                
                # PRINT ONE ROUND OF ALGS
                print("Current round of algs:")
                for alg in one_ripple_round_of__final_strTypeAlgs:
                    print(alg)
                    # WHY DOES IT APPEAR THAT SOME ROUNDS AREN'T PRINTING TO CONSOLE???


                if trailing_YorZ_Xs[0] == "Y0" or trailing_YorZ_Xs[0] == "Z0":
                    print("YorZ is either Y0 or X0. Only one get_combos() call is necessary. We are done finding algs")
                    break    # avoid creating duplicates. No need to ripple a zero-effect turn through and keep doing comp_Xpansion. By including the break HERE, a Y0 (or Z0) may ripple in a couple times, if the alg ends with U or U D.  I can live with that. There will still only be one Xpansion performed.  


            #  RIPPLE LEFT one time
            #  these two lines swap two elements of the list.  The YorZ component is always one of the two. It is rippling through.  
            #  note that, by design, the code only reaches the following lines if indx > 0
            add_YorZ__shifting_listTypeAlg[indx] = df_Ripple_L.at[add_YorZ__shifting_listTypeAlg[indx - 1], "A%s-->%sB"%(trailing_YorZ_Xs[0], trailing_YorZ_Xs[0])]
            add_YorZ__shifting_listTypeAlg[indx - 1] = trailing_YorZ_Xs[0]
    

    # Why is this next line in the generate_algs() method?  It should be called from main.py as a separate thing. This is just confusing and too much here
    from_single_SS__final_strTypeAlgs = insert_merge_YU_algs(ALL_ripple_rounds_from_single_SS__strTypeAlgs)
       
            
    return from_single_SS__final_strTypeAlgs
        

