import httpx

chostic_url = "https://www.chosic.com/api/tools/"

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
        "user-agent": "Mozilla/5.0",
        "referer": "https://www.chosic.com/playlist-generator/",
        "x-requested-with": "XMLHttpRequest",
        "x-wp-nonce": "",
        "accept": "application/json"
    }
    return headers