from fpdf import FPDF

# Cleaned version of readme text (no box drawing characters)
readme_text = """
Spotify Music Recommendation System
===================================

This project is a Spotify-like music recommender system built using Machine Learning and Streamlit for a simple and interactive user interface.

It takes a song as input and recommends 5 similar songs based on audio features using cosine similarity.

Project Structure
-----------------
spotify_recommender/
  - app.py                  # Main Streamlit GUI app
  - data/
    - spotify_dataset.csv   # Music dataset (features & metadata)
  - README.md               # Project instructions (this file)

Features Used
-------------
The model uses the following Spotify audio features to calculate similarity:
- Acousticness
- Danceability
- Energy
- Instrumentalness
- Liveness
- Speechiness
- Valence
- Tempo

How to Run
----------
Requirements:
- Python 3.7+
- pip

Install Dependencies:
    pip install streamlit pandas numpy scikit-learn

Run the App:
    cd spotify_recommender
    streamlit run app.py

Or if 'streamlit' command doesn't work:
    python -m streamlit run app.py

Usage
-----
1. Open the app in your browser (usually opens automatically).
2. Choose a song from the dropdown.
3. Click "Recommend Similar Songs".
4. Get top 5 similar songs based on audio features!

Dataset Info
------------
The dataset is located in data/spotify_dataset.csv and contains:
- track_name
- artist_name
- Audio feature columns (numerical values used for similarity)

How It Works
------------
1. Dataset is preprocessed and scaled using StandardScaler.
2. Similarity between songs is calculated using cosine_similarity.
3. The 5 most similar songs are recommended excluding the input song.

Future Improvements
-------------------
- Add genre and mood filters
- Use deep learning for more personalized recommendations
- Add audio preview and album art

Author
------
Abdulahad (aka Eleven)
Built with love and Python

License
-------
This project is for educational purposes and freely available to use and modify.
"""

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

for line in readme_text.split('\n'):
    pdf.multi_cell(0, 10, line)

# Save PDF
pdf_path = "/mnt/data/Spotify_Recommender_README.pdf"
pdf.output(pdf_path)

pdf_path
