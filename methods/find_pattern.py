from variables.constants import REPLACEMENTS_DICT, HEADER, SOLVED_PATTERN_LETTERS
from variables.dataframes import df_stickers_turned

def find_pattern(stic_alg):

	# convert alg from string to list:
	stic_alg = stic_alg + " "
	for key, value in REPLACEMENTS_DICT.items():
		stic_alg = stic_alg.replace(key, value) # remove (, ],  replace M' with T,  etc.
		stic_alg = " ".join(stic_alg.split())  # remove internal duplicate spaces 
	turns = list(stic_alg.strip().split(" "))



	# The HEART of the method:
	# starting with solved state:
	pattern = ["wht", "grn", "red", "blu", "ora", "yel", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"]
	for turn in turns:
		for i in range(len(pattern)):
			pattern[i] = df_stickers_turned.at[pattern[i], HEADER[turn]]



	inverse_pattern_tuple_list = []
	for i in range(len(SOLVED_PATTERN_LETTERS)):
		inverse_pattern_tuple_list.append((pattern[i], SOLVED_PATTERN_LETTERS[i]))  # create list of tuples
	inverse_pattern_dict = dict((x,y) for x,y in inverse_pattern_tuple_list)
	
	pattern_letters = []
	for letter in SOLVED_PATTERN_LETTERS:
		pattern_letters.append(inverse_pattern_dict[letter])



	return pattern_letters