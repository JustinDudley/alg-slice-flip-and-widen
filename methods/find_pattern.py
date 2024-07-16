from variables.constants import REPLACEMENTS_DICT, HEADER
from variables.dataframes import df_stickers_turned

def find_pattern(strTypeAlg):

	# convert alg from string to list:
	strTypeAlg = strTypeAlg + " "
	for key, value in REPLACEMENTS_DICT.items():
		strTypeAlg = strTypeAlg.replace(key, value) # remove (, ],  replace M' with T,  etc.
		strTypeAlg = " ".join(strTypeAlg.split())  # remove internal duplicate spaces 
	listTypeAlg = list(strTypeAlg.strip().split(" "))



	# The HEART of the program:
	# starting with solved state:
	pattern = ["wht", "grn", "red", "blu", "ora", "yel", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"]
	for turn in listTypeAlg:
		for i in range(len(pattern)):
			pattern[i] = df_stickers_turned.at[pattern[i], HEADER[turn]]



	solved_pattern = ["wht", "grn", "red", "blu", "ora", "yel", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"]
	inverse_pattern_tuple_list = []
	for i in range(len(solved_pattern)):
		inverse_pattern_tuple_list.append((pattern[i], solved_pattern[i]))  # create list of tuples
	inverse_pattern_dict = dict((x,y) for x,y in inverse_pattern_tuple_list)
	
	listTypePattern = []
	for letter in solved_pattern:
		listTypePattern.append(inverse_pattern_dict[letter])



	return listTypePattern