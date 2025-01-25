import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

mv_d=pd.read_csv('movies.csv')
s_fea=mv_d[['genres','keywords','tagline','cast','director']]
for f in s_fea:
  mv_d[f]=mv_d[f].fillna('')

com = mv_d['genres'] + ' ' + mv_d['keywords'] + ' ' + mv_d['tagline'] + ' ' + mv_d['cast'] + ' ' + mv_d['director']

vectorizer=TfidfVectorizer()
f_vectors=vectorizer.fit_transform(com)

sim=cosine_similarity(f_vectors)

mv_m=input('Enter Your Fav Movie Name:')

list_all=mv_d['title'].tolist()

find=difflib.get_close_matches(mv_m,list_all)

cmatch=find[0]

index_m=mv_d[mv_d.title==cmatch]['index'].values[0]

sim_score=list(enumerate(sim[index_m]))

sort_sim_m=sorted(sim_score,key=lambda x:x[1] ,reverse=True)
print('Movies suggested for you : \n')

i = 1

for movie in sort_sim_m:
  index = movie[0]
  title_from_index = mv_d[mv_d.index==index]['title'].values[0]
  rating=mv_d[mv_d.index==index]['vote_average'].values[0]
  time=mv_d[mv_d.index==index]['runtime'].values[0]
  if (i<10):
    print(i, '.',title_from_index,'-',rating,'Duration:',time)
    i+=1