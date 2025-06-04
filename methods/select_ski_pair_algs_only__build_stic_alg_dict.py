
from variables.constants import SKI_PAIRS


def select_ski_pair_algs_only__build_stic_alg_dict(stic_algs):

    stic_alg_dicts = []


    # for each alg:  The alg and an associated boolean are put into a dictionary.
    # in THIS branch, the boolean is kept though it is redundant. ALL booleans will be TRUE
    for alg in stic_algs:

        alg = alg + " "    #add white space so that SKI_PAIRS works

        ski_pair_counter = 0
        for ski_pair in SKI_PAIRS:
            if alg.find(ski_pair) != -1:   # we found one ski_pair, in step 1 of this iteration
                ski_pair_counter += 1
            if alg.find(ski_pair) != alg.rfind(ski_pair):  # in step 2 of this iteration, we found at least one additional ski_pair IN THE SAME ITERATION.  Note "rfind" finds the right-most occurence of a substring
                ski_pair_counter += 1
        

        if ski_pair_counter == 1:   # THIS is the only case we're interested in. Where there is exactly one ski_pair in the whole alg. For all other cases, the alg does not move forward in the process. It dies here.

            alg = " ".join(alg.split()).rstrip()  # remove all internal and trailing whitespace. Creates a python list for one millisecond, then turns it back into a string

            # add alg, and an associated boolean, to a list of dictionaries.  In THIS branch, the boolean is kept though it is redundant. ALL booleans will be TRUE
            stic_alg_dict = {"alg": alg, "has_exactly_one_ski_pair": True}  # the index will be set later, AFTER compoundify
            stic_alg_dicts.append(stic_alg_dict)



    return(stic_alg_dicts)
