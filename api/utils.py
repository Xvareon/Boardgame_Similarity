import requests
from bs4 import BeautifulSoup
import numpy as np
from .fetch_games import fetch_top_100_games

# Get the top 100 game IDs
TOP_100_WITH_NAMES = fetch_top_100_games()
TOP_100_GAME_IDS = [gid for gid, _ in TOP_100_WITH_NAMES]


def get_user_ratings(username, top_games=TOP_100_GAME_IDS):
    # Scrape BGG user collection and return {game_id: rating} for top games.
    ratings = {}
    try:
        page = 1
        while True:
            url = f"https://boardgamegeek.com/collection/user/{username}?rated=1&page={page}"
            response = requests.get(url)
            if response.status_code != 200:
                break
            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.select("tr[id^='row_']")
            if not rows:
                break

            for row in rows:
                game_link = row.find('a', class_='primary')
                if not game_link:
                    continue
                href = game_link['href']
                game_id = int(href.split('/')[2])
                if game_id not in top_games:
                    continue

                # User rating column
                rating_td = row.find('td', class_='collection_bggrating')
                if rating_td:
                    try:
                        rating = float(rating_td.text.strip())
                    except:
                        rating = 0.0
                    ratings[game_id] = rating

            page += 1

    except Exception:
        return {}  # If user not found or scraping fails

    return ratings


def cosine_similarity(ratings1, ratings2, top_games=TOP_100_GAME_IDS):
    """
    Compute cosine similarity between two users' ratings.
    """
    vec1 = np.array([ratings1.get(gid, 0) for gid in top_games])
    vec2 = np.array([ratings2.get(gid, 0) for gid in top_games])
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0.0
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))