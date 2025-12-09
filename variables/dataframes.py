import pandas as pd 

df_Ripple_L = pd.read_csv('tables/WCR_Ripples_Left.csv', index_col="orig") 
df_Ripple_R = pd.read_csv('tables/WCR_Ripples_Right.csv', index_col="orig") 
df_turn_attributes = pd.read_csv('tables/turn_attributes.csv', index_col="orig") 

df_stickers_turned = pd.read_csv('tables/stickers_turned_by_alg_notation.csv', index_col="orig") 
df_stickers_rotated = pd.read_csv('tables/stickers_rotated_24.csv', index_col="orig") 
df_stickers_reflected = pd.read_csv('tables/stickers_reflected_24.csv', index_col="orig")




# print("df_Ripple_L:\n\n", df_Ripple_L, "\n")
# print("df_Ripple_R:\n\n", df_Ripple_R, "\n")
# print("turn_attributes:\n\n", df_turn_attributes, "\n")

# print("df_stickers_turned:\n\n", df_stickers_turned, "\n")
# print("df_stickers_rotated:\n\n", df_stickers_rotated, "\n")
# print("df_stickers_reflected:\n\n", df_stickers_reflected, "\n")