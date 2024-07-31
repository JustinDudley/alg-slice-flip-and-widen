
# This is a regretable patch.
# The program will probably take a performance hit.
# AND it's chintzy:  I am solving the "... Y U" problem but not even address the "...Y U D" problem.
# I'm not addressing the second problem because I am going to filter out those algs anyway. But I am creating an incomplete alg list, which I do not like.


# Rationale for this method:
# a trailing YorZ next to a U, U', U2, D, D', D2 (or for Z:  F, F', F2, B, B', B2)  gets rippled left BEFORE itertools
# has a chance to analyze it. This is done to avoid functional duplicates.
#  (It was easier to create logic to ripple THEN do itertools than to do itertools then ripple.)
# But what I lose is an alg that ends with something like "... U Y". I actually DO want to see these and consider these.
# So in this method, I take algs that end in, for instance, "... Y U", and I append/insert another alg that has the last two
# turns reversed. So, the inserted alg ends with "... U Y".
# The original alg is kept. Nothing is lost. This method only inserts a few new algs.



# adapted from the interweb.  This method reverses the last two items in a list
def reverse_last_two_items(list):
    size = (len(list) - 1) + (len(list) - 2)   # indexes of final and penultimate items of list, respectively
    for i in range(len(list) - 2, (size + 1) // 2):
        j = size - i
        list[i], list[j] = list[j], list[i]
    
    return list




def insert_reinstated_trailing_YorZ__patch(one_ripple_round_of__final_algs):
    
    trailing_YorZ_reinstated__one_ripple_round_of__final_algs = []
    for alg in one_ripple_round_of__final_algs:
        trailing_YorZ_reinstated__one_ripple_round_of__final_algs.append(alg)


        for Y_or_Z_turn in ["Y", "Z"]:     # to increase performance. Check last-6-character substring of alg for the presence of Y or Z before procedding
            if alg[len(alg) - 6:].find(Y_or_Z_turn) >= 0:



                turns = alg.split()
                if len(turns) > 5: # this prevents an out-of-range error. It rules out too-short list elements that AREN'T algs, namely the elements added by my testing suite that are simply WORDS

                    if turns[-2] in ["Y", "Y'", "Y2"] and turns[-1] in ["U", "U'", "U2", "D", "D'", "D2", "H", "H'", "H2"]:
                        turns = reverse_last_two_items(turns)
                        temp_alg = " ".join(turns)
                        trailing_YorZ_reinstated__one_ripple_round_of__final_algs.append(temp_alg)

                    elif turns[-2] in ["Z", "Z'", "Z2"] and turns[-1] in ["F", "F'", "F2", "B", "B'", "B2", "S", "S'", "S2"]:
                        turns = reverse_last_two_items(turns)
                        temp_alg = " ".join(turns)
                        trailing_YorZ_reinstated__one_ripple_round_of__final_algs.append(temp_alg)




    return trailing_YorZ_reinstated__one_ripple_round_of__final_algs
