import pandas as pd

# create a dataframe using final.csv file
df = pd.read_csv('final.csv')

# sorting dataframe : wrt to weighted rating col in ascending order
df = df.sort_values('weighted_rating' , ascending = False)

# final dataframe
output = df[['original_title' , 'poster_link' , 'runtime', 'release_date' , 'weighted_rating' ]].head(20)
