
import itertools
import math

from dataframes import df_comp_rotation_nums

def get_Sum_Successes_using_itertools(comp_turn_codes, trailing_YorZ_Xs):

    rotation_num = df_comp_rotation_nums.at[trailing_YorZ_Xs[1], "comp_rotation_num"]

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


    sum_successes = []
    for rotation_number_mod_4_comb in combos_of_positions_whose_comps_sum_correctly:
        sum_of_rotaion_number = []
        for i in range (0, len(comp_turn_codes)):
            if i in rotation_number_mod_4_comb:
                sum_of_rotaion_number.append(comp_turn_codes[i])
            else: sum_of_rotaion_number.append(0)
        sum_successes.append(sum_of_rotaion_number)

    print("\nsum_successes  (a.k.a.  Every possible   useful modification of comp_code_turns. Elements that sum correctly (mod 4) remain, and the rest are replaced by zeros):  ")
    print(sum_successes)
    print("\nNumber of new algs to generate:  ", len(sum_successes), "\n")

    return sum_successes

