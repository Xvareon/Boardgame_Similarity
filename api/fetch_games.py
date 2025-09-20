import requests
from bs4 import BeautifulSoup

def fetch_top_100_games():
    # Fetch top 100 BGG games (IDs + names) across multiple pages. Returns a list of tuples: (game_id, game_name)
    top_100_games = []

    # BGG shows 50 games per page; need 2 pages for top 100
    for page in range(1, 3):
        url = f"https://boardgamegeek.com/browse/boardgame/page/{page}"
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.select("tr[id^='row_']")

        for row in rows:
            if len(top_100_games) >= 100:
                break  # stop once we have 100 games
            game_link = row.find('a', class_='primary')
            if game_link:
                href = game_link['href']  # e.g., /boardgame/174430/gloomhaven
                game_id = int(href.split('/')[2])
                game_name = game_link.text.strip()
                top_100_games.append((game_id, game_name))

    return top_100_games

if __name__ == "__main__":
    top_100 = fetch_top_100_games()

    # Print with names (for reference)
    print("TOP_100_GAMES = [")
    for gid, name in top_100:
        print(f"    ({gid}, '{name}'),")
    print("]")