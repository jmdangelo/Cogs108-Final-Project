#code to clean up csv, removes all the states not from california and zip codes with 'X''s in them

import pandas
df = pandas.read_csv('new.csv')
#list(df)


#drops all the rows with non CA states
df2 = df.ix[~(df['State'] != 'CA')]

#df3= df2[['State']]
#print(df3)
#result = df2[['ZIP code']].contains(pat = 'XXX')


#drops all rows with missing zip codes
df2 = df2.dropna(subset=['ZIP code'])


# drops all rows with zip codes with 'X' in them
result = df2[~df2['ZIP code'].str.contains('X')]


#save to CSV file
result.to_csv("new2.csv", encoding='utf-8', index=False)
