
from variables.constants import ITERATIVE_DELTA_SWAP_DICT


def reversify_selected_algs__build_stic_alg_dict(stic_algs):

    stic_alg_dicts = []


    # for each alg:  The alg and an associated boolean are put into a dictionary. For a reversifiable alg, the reversified alg is ALSO put into a dictionary (along with its boolean)
    for alg in stic_algs:

        # (1) ADD ORIGINAL ALG, and an associated boolean, to a list of dictionaries
        stic_alg_dict = {"alg": alg, "is_reversified": False}
        stic_alg_dicts.append(stic_alg_dict)


        alg = alg + " "    #add white space so the TRI_TURN_SWAP_DICT works


        tri_turn_counter = 0
        for tri_turn_pair in ITERATIVE_DELTA_SWAP_DICT:
            if alg.find(tri_turn_pair) != -1:   # we found one tri-turn
                tri_turn_counter += 1
            if alg.find(tri_turn_pair) != alg.rfind(tri_turn_pair):  # we found at least one additional tri-turn.   Note "rfind" finds the right-most occurence of a substring
                tri_turn_counter += 1
        

        if tri_turn_counter == 1:   # THIS is the only case we're interested in. Where there is exactly one tri-turn in the whole alg. For all other cases, the method returns:  "Nothing to see here"
            for key, value in ITERATIVE_DELTA_SWAP_DICT.items():
                alg = alg.replace(key, value)   # "L R2" gets replaced by "R2 L", for instance
            alg = " ".join(alg.split()).rstrip()  # remove all internal and trailing whitespace



            # (2) ADD REVERSIFIED ALG, and an associated boolean, to a list of dictionaries
            stic_alg_dict = {"alg": alg, "is_reversified": True}  # the index will be set later, AFTER compoundify
            stic_alg_dicts.append(stic_alg_dict)



    return(stic_alg_dicts)




# This method adds a few internal Y (or Z) algs that would otherwise be missed.
# It doesn't affect leading Y or Z algs
# The idea is that when you have an alg containing R L (or U D2, or B' F...), you can reverse those 2 and
# the alg doesn't change its functionality. But when the Y ripples through, it creates a new unique alg ONLY at that
# one moment when the Y or Z is BETWEEN the two reversible-friendly turns.
# I believe it only changes TWO turns of the resultant alg:  The turns in the reversible-friendly pair. Everything else remains
# the same
# Surprisingly enough, this generates many new algs, and some survive the filtering process later, because a few of the 
# new algs NO LONGER have a B turn. (At least, that's what I think is going to happen).
# The idea is to hopefully finally get to the point where ALL inverses have been tracked down and discovered.
# Because right now I'm still missing a few.

# This is really just a patch. I'm only addressing algs that have exactly ONE reversible-friendly pair.
# For an alg with more than one, that whole alg and all its itertools buddies are going to get filtered out by 
# my filtering app anyway. That's why I'm not inserting EVERY possible reversal into the list of algs.