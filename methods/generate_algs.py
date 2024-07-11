
import copy

from methods.Mod4_Comp_Xpansion import Mod4_Comp_Xpansion
from variables.dataframes import df_rotation_nums
from methods.get_DNA_3_marker_cums import get_DNA_3_marker_cums_using_itertools
from methods.helper_methods import get_turn_codes


def generate_algs(alg_turns:list[str], trailing_YorZ_Xs_dual):

    final_algs_from_single_SticSolv = []

    for trailing_YorZ_Xs in trailing_YorZ_Xs_dual:

        alg_turns_plus_YorZ_static = copy.deepcopy(alg_turns) # no YorZ yet
        alg_turns_plus_YorZ_static.append(trailing_YorZ_Xs[0])  # YorZ appended
        alg_turns_plus_YorZ_shifting = copy.deepcopy(alg_turns_plus_YorZ_static)
        
        comp_turn_codes = copy.deepcopy(list(map(get_turn_codes, alg_turns_plus_YorZ_static)))
        DNA_3_marker_cums = get_DNA_3_marker_cums_using_itertools(comp_turn_codes, trailing_YorZ_Xs)


     
        # for index, alg_turn in reversed(list(enumerate(alg_turns_plus_YorZ_static))):
            # print("index and single alg_turn, in reverse order, are: ", index, ",  ", alg_turn) 

        # Need to re-indent the two lines below, and un-comment the "for index, alg_turn..."  two lines above    
        one_round_of_final_algs = Mod4_Comp_Xpansion(alg_turns_plus_YorZ_shifting, trailing_YorZ_Xs, DNA_3_marker_cums)
        final_algs_from_single_SticSolv.append(one_round_of_final_algs)   
            #Call the Ripple_L method, so YorZ moves one to the left before this loop repeats

    return final_algs_from_single_SticSolv
        

