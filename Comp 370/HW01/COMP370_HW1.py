import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## Part 1 - Data Collection
# Read in the CSV file


# df = pd.read_csv('https://github.com/fivethirtyeight/russian-troll-tweets/raw/master/IRAhandle_tweets_1.csv', index_col=0)
# df = df.head(10000)

# # Filter tweets that are in English (assuming there's a column named 'language' indicating the language)
# df = df[df['language'] == 'English']

# # Filter tweets that don't contain a question mark '?'
# df = df[~df['content'].str.contains('\?')]

# # Save the filtered DataFrame to a TSV file
# df.to_csv("filtered_tweets.tsv", sep='\t', index=False)

## Part 2 - Data Annotation 
# data=pd.read_csv('/Users/marie-eliselatorre/Downloads/filtered_tweets.tsv',sep='\t')
# data['trump_mention']= data["content"].str.contains(r'\bTrump\b', case=False, regex=True)
# data["trump_mention"] = data["trump_mention"].replace({True: "T", False: "F"})
# trump = data[["tweet_id","publish_date","content","trump_mention"]]
# trump.to_csv("/Users/marie-eliselatorre/Downloads/dataset.tsv", sep = '\t')

## Part 3 - Analysis
data=pd.read_csv('/Users/marie-eliselatorre/Downloads/dataset.tsv',sep='\t')
counts = data['trump_mention'].str.count('T')
rows_count = len(data.index)
print(rows_count)