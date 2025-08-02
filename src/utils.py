import httpx
import config
import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime

chostic_url = "https://www.chosic.com/api/tools/"

chostic_params = {
    'track': {
        'limit': 10,
        'seed': 'seed_tracks'
    },
    'artist': {
        'limit': 6,
        'seed': 'seed_artists'
    }
}

def fetch_auth_data():
    
    URL = "https://www.chosic.com/playlist-generator/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }
    
    try:
        session = requests.Session()
        session.headers.update(HEADERS)

        response = session.get(URL)
        response.raise_for_status()

        nonce = None
        match = re.search(r'"nonce":"([a-zA-Z0-9]+)"', response.text)
        if match:
            nonce = match.group(1)
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            for script in soup.find_all('script'):
                if script.string and 'nonce' in script.string:
                    match = re.search(r'nonce[:\s=]+["\']([a-zA-Z0-9]+)["\']', script.string)
                    if match:
                        nonce = match.group(1)
                        break

        if not nonce:
            raise ValueError("x-wp-nonce not found in page source")

        cookies = session.cookies.get_dict()

        auth_data = {
            "x-wp-nonce": nonce,
            "cookie_header": "; ".join([f"{k}={v}" for k, v in cookies.items()]),
            "timestamp": datetime.now().isoformat(),
            "user_agent": HEADERS["User-Agent"]
        }

        return auth_data

    except Exception as e:
        print("❌ Error:", str(e))
        return {
            "x-wp-nonce": nonce if nonce else None,
            "cookie_header": "; ".join([f"{k}={v}" for k, v in cookies.items()]) if cookies else None,
            "timestamp": datetime.now().isoformat(),
            "user_agent": HEADERS["User-Agent"]
        }

def convert_image_to_large(image_url: str):
    """
    Args:
        image_url (str): url of small size image.
        
    Returns:
        str: url of big size image.
    """        
    if "4851" in image_url:
        image_url = image_url.replace("4851", "b273")

    return image_url

def get_response(url, params, headers):
    result = {
        "success": True,
        "message": "Operation successful",
        "data": {}
    }
    
    try:
        response = httpx.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            raw = response.json()
            result["data"] = raw
            
        else:
            result["success"] = False
            result["message"] = f"HTTP {response.status_code}"

    except Exception as e:
        result["success"] = False
        result["message"] = f"Exception: {str(e)}"

    return result


def get_chosic_headers():
    auth_data = fetch_auth_data()
    
    headers = {
    "authority": "www.chosic.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,fa;q=0.8",
    "app": "playlist_generator",
    "cookie": auth_data['cookie_header'],
    "priority": "u=1, i",
    "referer": "https://www.chosic.com/playlist-generator/",
    
    "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-wp-nonce": auth_data['x-wp-nonce']
    }
    return headers