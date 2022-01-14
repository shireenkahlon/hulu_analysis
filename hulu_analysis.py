#import pandas and datetime
import pandas as pd
import datetime

#read in hulu_genre.csv and hulu_watch_history.csv
genre_df = pd.read_csv('hulu_genre.csv')
watch_df = pd.read_csv('hulu_watch_history.csv')

#print the head of genre_df and watch_df
print(genre_df.head())
print(watch_df.head())

#remove Unnamed: 2 from genre_df
genre_df = genre_df.drop(columns=['Unnamed: 2'])
print(genre_df.head())

#drop nulls from watch_df
watch_df = watch_df.dropna()
print(watch_df)

#convert last played at to datetime
watch_df['Last Played At'] = pd.to_datetime(watch_df['Last Played At'])

# seperate date and time from last played at in watch_df
# create 2 new columns for date and time
watch_df['Watch_Date'],watch_df['Watch_Time']= watch_df['Last Played At'].apply(lambda x:x.date()), watch_df['Last Played At'].apply(lambda x:x.time())

#delete the last played at column
watch_df = watch_df.drop(columns=['Last Played At'])

#print the head of watch_df
print(watch_df.head())

#convert genre_df to csv
genre_df.to_csv('hulu_genre_clean.csv')

#convert watch_df to csv
watch_df.to_csv('hulu_watch_history_clean.csv')