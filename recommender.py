# recommender.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from dataset import songs

# Prepare dataset
df = pd.DataFrame(songs)
df["metadata"] = df[["title", "artist", "genre", "tags"]].apply(lambda x: " ".join(x), axis=1)

# TF-IDF model
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["metadata"])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Recommendation function
def get_recommendations(song_id, top_n=20):
    idx = df.index[df["id"] == song_id][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1: top_n+1]
    song_indices = [i[0] for i in sim_scores]
    return df.iloc[song_indices].to_dict(orient="records")
