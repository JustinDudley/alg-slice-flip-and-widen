
import copy

from Mod4_Comp_Xpansion import Mod4_Comp_Xpansion
from dataframes import df_comp_rotation_nums
from get_Sum_Successes import get_Sum_Successes_using_itertools
from helper_methods import get_comp_turn_codes


def generate_algs(alg_turns:list[str], trailing_YorZ_Xs_dual):

    final_algs_from_single_SticSolv = []

    for trailing_YorZ_Xs in trailing_YorZ_Xs_dual:

        alg_turns_plus_YorZ_static = copy.deepcopy(alg_turns) # no YorZ yet
        alg_turns_plus_YorZ_static.append(trailing_YorZ_Xs[0])  # YorZ appended
        alg_turns_plus_YorZ_shifting = copy.deepcopy(alg_turns_plus_YorZ_static)
        comp_turn_codes = copy.deepcopy(list(map(get_comp_turn_codes, alg_turns_plus_YorZ_static)))
        sum_successes = get_Sum_Successes_using_itertools(comp_turn_codes, trailing_YorZ_Xs)
        print("alg_turns_plus_YorZ_static is: ", alg_turns_plus_YorZ_static, "\n")


        for index, alg_turn in reversed(list(enumerate(alg_turns_plus_YorZ_static))):
            print("index and single alg_turn, in reverse order, are: ", index, ",  ", alg_turn) 
            
            one_round_of_final_algs = Mod4_Comp_Xpansion(alg_turns_plus_YorZ_shifting, trailing_YorZ_Xs, sum_successes)
            final_algs_from_single_SticSolv.append(one_round_of_final_algs)   
            print("Here is final_alg_pipe_string so far: ", final_algs_from_single_SticSolv, "\n")
            #Call the Ripple_L method, so YorZ moves one to the left before this loop repeats

    return final_algs_from_single_SticSolv
        

