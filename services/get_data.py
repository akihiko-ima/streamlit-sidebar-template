import requests
from typing import Union, Dict, Any


def get_data() -> Union[Dict[str, Any], Dict[str, Union[int, str]]]:
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            'status_code': response.status_code,
            'error': response.text
        }
