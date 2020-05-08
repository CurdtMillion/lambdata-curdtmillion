from pandas import DataFrame

# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. 
# (Handle Washington DC and territories like Puerto Rico etc.)

df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
print(df.head())
