# app.py
from flask import Flask, render_template
from dataset import songs
from recommender import get_recommendations

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", songs=songs)

@app.route("/song/<int:song_id>")
def song_detail(song_id):
    song = next((s for s in songs if s["id"] == song_id), None)
    recommendations = get_recommendations(song_id)
    return render_template("song.html", song=song, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
