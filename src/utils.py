import httpx
import config

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
    headers = {
    "authority": "www.chosic.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,fa;q=0.8",
    "app": "playlist_generator",
    "cookie": config.user_cookie,
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
    "x-wp-nonce": config.xwp
    }
    return headers