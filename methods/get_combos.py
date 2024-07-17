
import itertools
import math

from variables.constants import CODE


def get_combos(alg_rotation_codes, trailing_YorZ_Xs):

    # trailing_X_rotation_num = df_rotation_codes_ELIMINATE_SOON.at[trailing_YorZ_Xs[1], FWD_ROTATION_CODE]
    trailing_X_rotation_num = CODE[trailing_YorZ_Xs[1]]
    positions_of_X_axis_turns = []
    for i in range (0, len(alg_rotation_codes)):
        if alg_rotation_codes[i] > 0:
            positions_of_X_axis_turns.append(i)

    combos = []
    for i in range(1, len(positions_of_X_axis_turns) + 1):
        els = [list(x) for x in itertools.combinations(positions_of_X_axis_turns, i)]
        combos.extend(els)
  

    combos_of_positions_whose_comps_sum_correctly:list[list[int]] = []   # "good_position_combos"
    for combo in combos:
        sum = 0
        for p in combo:
            sum = sum + alg_rotation_codes[p]
        if math.fmod(sum,4) == trailing_X_rotation_num:
            combos_of_positions_whose_comps_sum_correctly.append(combo)



    # create DNA_1
    DNA_1_sum_successes = []
    for good_combo in combos_of_positions_whose_comps_sum_correctly:
        sum_of_rotation_number = []
        for i in range (0, len(alg_rotation_codes)):
            if i in good_combo:
                sum_of_rotation_number.append(alg_rotation_codes[i])
            else: sum_of_rotation_number.append(0)
        DNA_1_sum_successes.append(sum_of_rotation_number)

    print("\nDNA_1_sum_successes  (a.k.a.  Every possible   useful modification of comp_code_turns. Elements that sum correctly (mod 4) remain, and the rest are replaced by zeros):  ")
    print("\n", DNA_1_sum_successes)
    print("\nSo, the number of new algs to generate (and print to console below) is:  ", len(DNA_1_sum_successes), "\n")


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
                DNA_3_marker_cum.append(CODE[DNA_2_mod4_core_turn_cumulatives[ind][index]])
        DNA_3_marker_cums.append(DNA_3_marker_cum)

    
    return DNA_3_marker_cums

