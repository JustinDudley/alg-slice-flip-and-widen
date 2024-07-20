
import itertools
import math

from variables.constants import CODE


def itertools_get_combos(alg_turn_codes, trailing_YorZ_Xs):

    # comp of a turn_code === turn_code of a complementary turn.  The rotation caused by the turn's complement IS the newly induced rotation of the cube, and the sum of those newly induced rotations must equal, mod 4, the code of the WCR's X-axis component
    alg_comp_turn_codes = list(map(lambda x: (4-x)%4, alg_turn_codes))
    
    print("\nalg_turn_codes, specific to the turn that YorZ is next to:  ", alg_turn_codes)
    print("alg_comp_turn_codes, also specific to what YorZ is next to: ", alg_comp_turn_codes)


    positions_of_X_axis_turns = []
    for indx, turn_code in enumerate(alg_comp_turn_codes):
        if turn_code > 0:   # true for X-axis turns like R, L2,...  Finding those turns is the only goal of this loop
            positions_of_X_axis_turns.append(indx)


    combos = []
    for i in range(1, len(positions_of_X_axis_turns) + 1):
        els = [list(x) for x in itertools.combinations(positions_of_X_axis_turns, i)]
        combos.extend(els)
  

    trailing_X_rotation__target_num = CODE[trailing_YorZ_Xs[1]]
    combos_of_positions_whose_comps_sum_correctly:list[list[int]] = []
    for combo in combos:
        sum = 0
        for position in combo:
            sum = sum + alg_comp_turn_codes[position]   # Summing the COMPLEMENTS of different combinations of R, L turns
        if math.fmod(sum,4) == trailing_X_rotation__target_num:
            combos_of_positions_whose_comps_sum_correctly.append(combo)



    # create DNA_1      -- Here, we are NOT determining what happens to the X-axis turns, but rather what happens to EVERY OTHER TURN. Take the case of a WCR of X (turn_code 1):  We notice that we can replace a single R' with l'. So:  R' == l' X'.  The X' is placed in DNA_3 for each subsequent turn. Later, in comp_Xpansion, the X' will ripple right, changing each turn on its way and ultimately cancelling out the WCR of X. (That's my story and I'm sticking to it!)
    # Each sum_success is a just copy of alg_turn_codes but with some elements changed to 0. The elements left untouched are those which, together, sum to the target value. NOT TRUE
    DNA_1__sum_successes = []
    for good_combo in combos_of_positions_whose_comps_sum_correctly:
        alg_turn_codes___but_where_codes_with_badly_summing_comps_get_voted_off_the_island = []
        for i, alg_turn_code in enumerate(alg_turn_codes):
            if i not in good_combo:
                alg_turn_codes___but_where_codes_with_badly_summing_comps_get_voted_off_the_island.append(0)
            else: alg_turn_codes___but_where_codes_with_badly_summing_comps_get_voted_off_the_island.append(alg_turn_code)
        DNA_1__sum_successes.append(alg_turn_codes___but_where_codes_with_badly_summing_comps_get_voted_off_the_island)

    print("\nDNA_1_sum_successes  (a.k.a.  Every possible useful modification of alg_turn_codes. Groups of elements that sum correctly with each other (mod 4) remain, and the rest are replaced by zeros):  ")
    print("\n", DNA_1__sum_successes)
    print("\nSo, the number of new algs to generate (and print to console below) is:  ", len(DNA_1__sum_successes), "\n")


    # create DNA_2
    DNA_2__mod4_core_turn_cumulatives = []
    for DNA_1_sum_success in DNA_1__sum_successes:
        DNA_2_mod4_core_turn_cumulative = []
        for index, comp_rotation in enumerate(DNA_1_sum_success):
            if index == 0:
                DNA_2_mod4_core_turn_cumulative.append(comp_rotation)
            else:
                DNA_2_mod4_core_turn_cumulative.append((DNA_2_mod4_core_turn_cumulative[index - 1] + comp_rotation) % 4)
        DNA_2__mod4_core_turn_cumulatives.append(DNA_2_mod4_core_turn_cumulative)


    # create DNA_3
    DNA_3__marker_cums = []
    for ind, DNA_1_sum_success in enumerate(DNA_1__sum_successes):
        DNA_3_marker_cum = []
        for index, comp_rotation in enumerate(DNA_1_sum_success):
            if comp_rotation > 0:
                DNA_3_marker_cum.append("*")
            else:
                DNA_3_marker_cum.append(CODE[DNA_2__mod4_core_turn_cumulatives[ind][index]])
        DNA_3__marker_cums.append(DNA_3_marker_cum)
    

    return DNA_3__marker_cums
