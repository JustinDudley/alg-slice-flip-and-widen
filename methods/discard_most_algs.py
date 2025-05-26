
def discard_most_algs(all_algs):
    
    good_subset_of_algs = []
    for alg in all_algs:

        # include algs with u,d,f,b
        for turn_letter in ["u", "d", "f", "b"]:
            if alg.find(turn_letter) >=0:
                good_subset_of_algs.append(alg)


        # include algs whose SECOND turn (after the leading X) is a Y or Z WCR  (includes Y', Z2, etc.)
        first_whitespace_index = alg.find(" ")
        if alg[first_whitespace_index + 1] in ["Y", "Z"]:
            good_subset_of_algs.append(alg)
        

         # include algs whose FINAL turn is a Y or Z WCR  (includes Y', Z2, etc.)
        last_whitespace_index = alg.rfind(" ")
        if alg[last_whitespace_index + 1] in ["Y", "Z"]:
            good_subset_of_algs.append(alg)       


    return good_subset_of_algs