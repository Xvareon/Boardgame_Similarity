from boardgamegeek import BGGClient
import numpy as np
from .constants import TOP_100_GAMES

bgg = BGGClient()

def get_user_ratings(username, top_games=TOP_100_GAMES):
    # Return a dict of {game_id: rating} for a user
    try:
        user_collection = bgg.collection(username=username, rated=True)
        ratings = {g.id: g.rating for g in user_collection if g.id in top_games}
        return ratings
    except Exception:
        return {}  # Return empty if user not found or API fails

def cosine_similarity(ratings1, ratings2, top_games=TOP_100_GAMES):
    # Compute cosine similarity between two users
    vec1 = np.array([ratings1.get(gid, 0) for gid in top_games])
    vec2 = np.array([ratings2.get(gid, 0) for gid in top_games])
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0.0
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))