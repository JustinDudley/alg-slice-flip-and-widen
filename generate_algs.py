
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
            
            single_round_of_final_algs_pipe_string = calculate_XComps_with_itertools(alg_turns, trailing_WCRs)
            final_alg_pipe_string += single_round_of_final_algs_pipe_string
            print("Here is final_alg_pipe_string so far: ", final_alg_pipe_string)
            #Call the Ripple_L method, so YorZ moves one to the left before this loop repeats

        

