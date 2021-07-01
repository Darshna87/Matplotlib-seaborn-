# Movie recommondation using Item Based recommondation System

import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('white')

warnings.filterwarnings('ignore')

#read the file for ratings by users

column_names=['user_id','item_id','rating','timestamp']
id_df = pd.read_csv("./ml-100k/u.data",sep='\t',names=column_names)
print(id_df.head())
print(id_df.shape)

print('No of users: ', id_df['user_id'].nunique())
print('No. of movies:', id_df['item_id'].nunique())

#read the file of movie_is with movie_title

movie_df=pd.read_csv("./ml-100k/u.item",sep='|',header=None)
movie_df = movie_df.get([0,1])
movie_df.columns=['item_id','title']
print(movie_df.head())
print(movie_df.shape)

#merging both df into one based on item_id to get movie name

df=pd.merge(id_df,movie_df,on='item_id')
print(df.tail(n=3))


ratings=pd.DataFrame(df.groupby('title').mean()['rating'])
#print(ratings)

ratings['No of ratings']=pd.DataFrame(df.groupby('title').count()['rating'])

print(ratings.sort_values(by='rating',ascending=False))

#histogram of distribution

plt.figure(figsize=(10,6))
plt.hist(ratings['No of ratings'],bins=70)
plt.xlabel('No of times movie has been rated')

plt.figure(figsize=(10,6))
plt.hist(ratings['rating'],bins=70)
plt.xlabel('Average rating')

sns.jointplot(x='rating',y='No of ratings',data=ratings,alpha=0.7)

plt.show()

#finding correlation with each movie

moviematrix=df.pivot_table(index='user_id',columns='title',values='rating')

print(moviematrix)

def recommond_similar_movie(movie):
    movie_user_ratings=moviematrix[movie]

    #converting matrix into dataframe
    corr_movie=pd.DataFrame(moviematrix.corrwith(movie_user_ratings),columns=['correlation'])
    corr_movie.dropna(inplace=True)

    #considering only those having no of ratings more than 100
    corr_movie=corr_movie.join(ratings['No of ratings'])
    corr_movie=corr_movie[corr_movie['No of ratings']>100].sort_values('correlation',ascending=False)

    predictions=corr_movie.head(n=5)
    return predictions

print("=============Raiders of the Lost Ark (1981)===================")
print(recommond_similar_movie('Raiders of the Lost Ark (1981)'))
print("============As Good As It Gets (1997)====================")
print(recommond_similar_movie('As Good As It Gets (1997)'))