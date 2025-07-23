# Chosic Scraper

![banner](assets/banner.png)

**Chosic Scraper** is a tool for extracting rich data from <a href="https://www.chosic.com">Choisc.com</a> using web scraping.

⚠️ This project is unofficial and purely for educational purposes. No official Chosic API used.

<br>

## 📦 Installation

```bash
git clone https://github.com/Abssdghi/chosic_scraper.git
cd chosic_scraper
pip install -r requirements.txt
```


<br>




## 🔧 Functions

| Function | Parameters | Description |
|----------|------------|-------------|
| `search(keyword, type='track')` | `keyword: str`, `type: str = 'track'` | Searches for tracks or artists on a keyword. Returns metadata like name, artist, and image. |
| `get_similar_songs(id, limit=100, type='track')` | `id: int`, `limit: int = 100`, `type: str = 'track'` | Fetches a list of similar songs based on the given seed ID. Returns details such as name, preview URL, album info, and popularity. |


Each function returns structured JSON.


<br>

## 🧠 Usage

Just import the scraper and call your function:

```python
from chosic_scraper import *

song = search(keyword="taste")['data']['tracks']['items'][0]
name = song['name']
artist = song['artist']
id = song['id']

print(f"\nSongs similar to {name} by {artist}:\n")

tracks = get_similar_songs(id=id, limit=10)['data']['tracks']
    
for i in tracks:
    print(i['artists'][0]['name'] + " - " + i['name'])

```

<br>

## 📄 License

This project is licensed under the [MIT License](LICENSE).

<br>

## 🌟 Give it a Star

If you found this useful, feel free to ⭐️ the repo and share it with others!

<br>

Made with ☕ and 🎧 by [Abbas Sadeghi](https://github.com/abssdghi)