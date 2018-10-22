"""
Insert code here for all the transformations you are going to do
"""
import pandas as pd

# •	Read the data/flights.csv dataset into Python
df = pd.read_csv("../../data/flights.csv")

# •	remove the column "DAY_OF_WEEK"
print(list(df))
del df['DAY_OF_WEEK']
print(list(df))

# •	rename the column "WHEELS_OFF" to "HAS_WHEELS"
print(list(df))
df.rename(columns={'WHEELS_OFF':'HAS_WHEELS'},
                   inplace=True)
print(list(df))


# •	slice the dataset row-wise into 4 equal-sized chunks
def chunkify(lst, n):
    return [lst[i::n] for i in range(n)]


chunks = chunkify(df, 4)



# total recored in CSV 499999
print(len(df.index))

# Each chunk has records 125000 and last one has 124999
# print no of records in each chunk

for x in chunks:
    print(len(x.index))
    print(len(x))
    print(x.shape[0])


# •	concatenate back the chucks produced above into 1 dataset


# •	get the slice of the dataset that is only relevant to the airline AA

aa = df[df.AIRLINE == 'AA']
print('dataset that is only relevant to the airline A is')
print(len(aa.index))


