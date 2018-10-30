"""
Insert code here for all the transformations you are going to do
"""
import pandas as pd
import numpy as np

# •	Read the data/flights.csv dataset into Python
df = pd.read_csv("../../data/flights.csv")
# df = pd.read_csv("./data/flights.csv")

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
concadinatedList = pd.concat(chunks)
print('concadination')
print(concadinatedList)

# •	get the slice of the dataset that is only relevant to the airline AA
airlineaa = df.loc[df['AIRLINE'] == 'AA']
print('dataset that is only relevant to the airline A is')
print(len(airlineaa.index))

# get the slice of the dataset where delay is <10 and destination is PBI
delay10 = df[(df.WEATHER_DELAY > 10) & (df.DESTINATION_AIRPORT == 'PBI')]
print('delay greater than 10 and destination is PBI')
print(delay10)


# Create a column "has_A", which contains 1 if the airline name contains the letter 'A', 0 otherwise
df['has_A'] = ['1' if 'A' in x else '0' for x in df['AIRLINE']]
print('has_A')
print(df.has_A)

# get a random sample of the rows in the dataframe
samplerow = df.sample(n=3)
print('samplerow')
print(samplerow)

# binarise the column "ORIGIN_AIRPORT"
# df["code"] = df["code"].apply(lambda x: x in mylist)

# Create a "Route" column by merging departure airport and destination airport
df['route'] = df['ORIGIN_AIRPORT'].astype(str)+'_'+df['DESTINATION_AIRPORT']
print('route')
print(df.route)

# fill the blanks in the AIR_SYSTEM_DELAY column with the average of the column itself
print(df['AIR_SYSTEM_DELAY'].isna().sum())
df['AIR_SYSTEM_DELAY'] = df['AIR_SYSTEM_DELAY'].fillna(df['AIR_SYSTEM_DELAY'].mean())
print("----------------------")
print(df['AIR_SYSTEM_DELAY'].isna().sum())

# Remove outliers for 'departure_delay' - remove rows in excess of 3 standard deviations from me]
#------------------------------------------------------------------------------
# accept a dataframe, remove outliers, return cleaned data in a new dataframe
# see http://www.itl.nist.gov/div898/handbook/prc/section1/prc16.htm
#------------------------------------------------------------------------------
def remove_outlier(df_in, col_name):
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
    print(df_out)
    return df_out

remove_outlier(df, 'DEPARTURE_DELAY')

# Calculate the mean "Departure_delay" for each airline, over the whole dataset
delay_airline = df[['AIRLINE', 'DEPARTURE_DELAY']].groupby('AIRLINE').mean()
print(delay_airline)

# The number of flights leaving before 12pm for each airline

# total_12_airline = df[['AIRLINE', 'DEPARTURE_TIME']].groupby('AIRLINE').count()
total_12_airline = df[df['AIRLINE'] > 0].groupby([df.index.hour, 'DEPARTURE_TIME'])
print('total_12_airline')

print(total_12_airline)
