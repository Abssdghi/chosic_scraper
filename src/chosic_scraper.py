from utils import *


def search(keyword: str, type: str = 'track') -> dict:
    """
    Search for tracks using chosic.com API.

    Args:
        keyword (str): The search keyword.
        type (str, optional): The type of search (default is 'track').

    Returns:
        dict: Response in format:
        {
            "success": bool,
            "message": str,
            "data": {
                "tracks": {
                    "items": [
                        {
                            "id": str,
                            "name": str,
                            "artist": str,
                            "image": str
                        }, ...
                    ]
                }
            }
        }
    """
    url = chostic_url + "search"
    
    params = {
        "q": keyword,
        "type": type,
        "limit": 10
    }
    
    headers = get_chosic_headers()
    
    return get_response(url, params, headers)


def get_recommendations(id: int, limit=100):
    """
    Args:
        id (int): track id (get with search func).
        limit (int): limit of tracks count.

    Returns:
        json: result in format:
        {
            "tracks": [
                {
                    "id": "",
                    "name": "",
                    "artists": [
                        {
                            "name":"",
                            "id":""
                        }, ...
                    ],
                    "preview_url": "",
                    "duration_ms":"",
                    "popularity":"",
                    "album": {
                        "name":	"",
                        "album_type": "",
                        "release_date": "",
                        "id": "",
                        "release_date_precision": "",
                        "image_default": "",
                        "image_large": ""
                    }
                }, ...
            ]
        }
        
    """
    url = chostic_url + "recommendations"
    
    params = {
        "seed_tracks": id,
        "limit": limit
    }
    
    headers = get_chosic_headers()
    
    return get_response(url, params, headers)


