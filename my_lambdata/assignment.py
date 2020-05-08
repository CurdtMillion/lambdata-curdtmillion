from pandas import DataFrame

# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. 
# (Handle Washington DC and territories like Puerto Rico etc.)

def add_state_names(my_df):
    # TODO: add a column of corresponding state names
    
    # dict w/ abbrev/name mappings
    # creat a new column that is a copy of the 1st, but mapped w/ the names
    # concat with axis=1

    names_map = {"CA":"Cali", "CO":"Colo", "CT":"Conn"}

    breakpoint()


    return my_df


if __name__ == "__main__":
    
    df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())
