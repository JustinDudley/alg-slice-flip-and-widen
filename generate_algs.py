
from calculate_XComps_with_itertools import *

def generate_algs(alg_turns, trailing_WCRs_dual):

    #  0. initialize empty string:  final_alg_pipe_string (local var, to be returned)

    #  0.2  Is this where I say "for trailing_WCR in trailing_WCR_2_list"  ??

        #  0.5:  start a loop (reverse/enumerate) for XComp--Collapsify--append--ripple--(repeat).  This is the loop where, if a rippling Y' finds itself next to ANY other Y-rotatio turn like U, D, H, u..., it just moves on and ripples to the Left again. I guess that happens with an IF statement in XComp

            #  1. call calculate_XComps_with_itertools  (returns a ??Python list?? of algs)
            #       -- this method will probably call Collapsify internally, to collapse Y U' into d'  for instance
            #       -- As soon as a final alg goes from list to string, I would call collapsify on it, generate one additional alg, and insert that RIGHT behind its immediate predecessor
            #       -- return a pipe-separated bunch of algs as a string.  This is the bunch of algs from ONE round, before rippling the YorZ Left.

            #  2. append the algs (in a pipe-separated form) to the local var initialized above:  final_alg_pipe_string.  Don't need a special method for this, just do it inline.
            #  3. call Ripple() method.  YorZ ripples Left one turn 


    final_alg_pipe_string = ""
    for trailing_WCRs in trailing_WCRs_dual:
        print("alg_turns is: ", alg_turns)
        for index, alg_turn in reversed(list(enumerate(alg_turns))):
            print("index and single alg_turn, in reverse order, are: ", index, ",  ", alg_turn) 
            single_round_of_final_algs_pipe_string = calculate_XComps_with_itertools(alg_turns, trailing_WCRs_dual)
            final_alg_pipe_string += single_round_of_final_algs_pipe_string
            print("Here is final_alg_pipe_string so far: ", final_alg_pipe_string)
            #Call the Ripple_L method, so YorZ moves one to the left before this loop repeats

        


    # Step 1:  Give a value to RotationNum, such as 1,2,...
    # Step 2:  Excel created comp_turn_codes (a Python list),   [0, 0, 0, 3, 1, 0, 0, 2, 0, 3, 1, 0, 1, 3, 0, 0, 2]
    #so:
    RotationNum = 1   # in this NEW python program, this will be deterrmined by the X element of alg--YorZ--X
    comp_turn_codes = [0, 0, 0, 3, 1, 0, 0, 2, 0, 3, 1, 0, 1, 3, 0, 0, 2]   # easy to derive from the alg

    # RIGHT NOW, THERE IS A MISMATCH BETWEEN ROTATIONNUM ("1") AND THE VERBIAGE OF "2" 

    import itertools
    import math

    positions = []
    for i in range (0, len(comp_turn_codes)):
        if comp_turn_codes[i] >0:
            positions.append(i)
        

    combs= []
    for i in range(1, len(positions)+1):
        els = [list(x) for x in itertools.combinations(positions, i)]
        combs.extend(els)
    #print("\nAll position combinations of non-zero elements:  ")
    #print(combs)


    #
    #  !!  Regarding "two_mod_4_combs" and "sum_of_2s":  TWO is no longer the only number used. I can use 0,1,2,or 3 via RotationNum. But I am retaining the variable names for now
    #

    two_mod_4_combs = []
    for comb in combs:
        sum = 0
        for p in comb:
            sum = sum + comp_turn_codes[p]
        if math.fmod(sum,4) == RotationNum:
            two_mod_4_combs.append(comb)

    print("comp_turn_codes is:  ", comp_turn_codes)
    print("\nAll position combinations of non-zero elements where the elements sum to 2 (mod 4):  ")
    print (two_mod_4_combs)


    sum_of_2s = []
    for two_mod_4_comb in two_mod_4_combs:
        sum_of_2 = []
        for i in range (0, len(comp_turn_codes)):
            if i in two_mod_4_comb:
                sum_of_2.append(comp_turn_codes[i])
            else: sum_of_2.append(0)
        sum_of_2s.append(sum_of_2)


    print("\nsum_of_2s  (a.k.a.  Every possible   useful modification of comp_code_turns. Elements that sum to 2 (mod 4) remain, and the rest are replaced by zeros):  ")
    print(sum_of_2s)

    print("\nNumber of new algs to generate:  ", len(sum_of_2s), "\n")


    # return a string:  a pipe-separated bunch of algs;  ALL the algs for a given StickerSolve alg
    return("hi|there|you|handsome|devil")
