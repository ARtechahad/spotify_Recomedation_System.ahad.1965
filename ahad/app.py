
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/spotify_dataset.csv")
    return df

# Preprocess features
def preprocess(df):
    features = ['acousticness', 'danceability', 'energy', 'instrumentalness',
                'liveness', 'speechiness', 'valence', 'tempo']
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(df[features])
    return df, data_scaled

# Recommend similar songs
def recommend(song_name, df, data_scaled):
    if song_name not in df['track_name'].values:
        return []
    index = df[df['track_name'] == song_name].index[0]
    similarity = cosine_similarity([data_scaled[index]], data_scaled)
    scores = list(enumerate(similarity[0]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    return [df.iloc[i[0]]['track_name'] + " by " + df.iloc[i[0]]['artist_name'] for i in scores]

# Streamlit GUI
st.set_page_config(page_title="🎧 Music Recommender", layout="centered")
st.title("🎶 Spotify-like Music Recommender System")

df = load_data()
df, data_scaled = preprocess(df)

selected_song = st.selectbox("Choose a song:", df['track_name'].dropna().unique())

if st.button("Recommend Similar Songs"):
    st.subheader("Top 5 Similar Songs:")
    recommendations = recommend(selected_song, df, data_scaled)
    for i, song in enumerate(recommendations, 1):
        st.write(f"{i}. {song}")
