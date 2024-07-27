
def remove_Y0_and_Z0(one_ripple_round_of__final_algs):

    streamlined_algs = []
    for alg in one_ripple_round_of__final_algs:
        alg = alg.replace("Y0", "")
        alg = alg.replace("Z0", "")
        alg = " ".join(alg.split())  # remove internal duplicate spaces 
        alg = alg.strip()

        streamlined_algs.append(alg)


    return(streamlined_algs)
