cols = ["A", "B", "C"]

def get_row_col(loc):
    return (int(loc[1]) - 1, cols.index(loc[0]))
    
print(get_row_col("A3"))
