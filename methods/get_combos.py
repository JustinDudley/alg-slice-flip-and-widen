
import itertools
import math

from variables.dataframes import df_rotation_nums
from variables.constants import CODE_TO_TURN

def get_combos(comp_turn_codes, trailing_YorZ_Xs):

    rotation_num = df_rotation_nums.at[trailing_YorZ_Xs[1], "comp_rotation_num"]

    positions_of_X_axis_turns = []
    for i in range (0, len(comp_turn_codes)):
        if comp_turn_codes[i] > 0:
            positions_of_X_axis_turns.append(i)

    combs = []
    for i in range(1, len(positions_of_X_axis_turns) + 1):
        els = [list(x) for x in itertools.combinations(positions_of_X_axis_turns, i)]
        combs.extend(els)
  

    combos_of_positions_whose_comps_sum_correctly:list[list[int]] = []   # "good_position_combos"
    for comb in combs:
        sum = 0
        for p in comb:
            sum = sum + comp_turn_codes[p]
        if math.fmod(sum,4) == rotation_num:
            combos_of_positions_whose_comps_sum_correctly.append(comb)

    print("comp_turn_codes is:  ", comp_turn_codes)
    print ("combos_of_positions_whose_comps_sum_correctly is: ", combos_of_positions_whose_comps_sum_correctly)



    # create DNA_1
    DNA_1_sum_successes = []
    for rotation_number_mod_4_comb in combos_of_positions_whose_comps_sum_correctly:
        sum_of_rotaion_number = []
        for i in range (0, len(comp_turn_codes)):
            if i in rotation_number_mod_4_comb:
                sum_of_rotaion_number.append(comp_turn_codes[i])
            else: sum_of_rotaion_number.append(0)
        DNA_1_sum_successes.append(sum_of_rotaion_number)

    print("\nDNA_1_sum_successes  (a.k.a.  Every possible   useful modification of comp_code_turns. Elements that sum correctly (mod 4) remain, and the rest are replaced by zeros):  \n")
    print(DNA_1_sum_successes)
    print("\nNumber of new algs to generate:  ", len(DNA_1_sum_successes), "\n")



    # create DNA_2
    DNA_2_mod4_core_turn_cumulatives = []
    for DNA_1_sum_success in DNA_1_sum_successes:
        DNA_2_mod4_core_turn_cumulative = []
        for index, comp_rotation in enumerate(DNA_1_sum_success):
            if index == 0:
                DNA_2_mod4_core_turn_cumulative.append(comp_rotation)
            else:
                DNA_2_mod4_core_turn_cumulative.append((DNA_2_mod4_core_turn_cumulative[index - 1] + comp_rotation) % 4)
        DNA_2_mod4_core_turn_cumulatives.append(DNA_2_mod4_core_turn_cumulative)
    

    # create DNA_3
    DNA_3_marker_cums = []
    for ind, DNA_1_sum_success in enumerate(DNA_1_sum_successes):
        DNA_3_marker_cum = []
        for index, comp_rotation in enumerate(DNA_1_sum_success):
            if comp_rotation > 0:
                DNA_3_marker_cum.append("*")
            else:
                DNA_3_marker_cum.append(CODE_TO_TURN[DNA_2_mod4_core_turn_cumulatives[ind][index]])
        DNA_3_marker_cums.append(DNA_3_marker_cum)

    
    return DNA_3_marker_cums

